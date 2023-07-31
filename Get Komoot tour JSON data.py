# This Python script retrieves data from the website "komoot.de," saves it as a JSON file, and processes the information related to tours made by the user. 

## We need to import two Python libraries.
# 1. *requests* library, to create sessions as well as getting and posting data
# 2. *json* library, to parse komoot data to JSON objects and vice versa
import requests
import json

## Set your credentials and client ID to access the komoot.de website
# The ID is located in the requested URL - log into komoot, go to your profile and take the id from the URL, it contains twelve digits
email = "<your email address to access komoot>"
password = "<your password>"
client_id = "<your client id>"

## set all variables
# define komoot url for login
login_url = "https://account.komoot.com/v1/signin"

# define komoot url for tour overview to get tour ids from
sport_types = ""
type = "tour_recorded"
sort_field = "date"
sort_direction = "desc"
name = ""
status = "" # private
hl = "de"
page = ""
limit = "50" # standard is 24
tour_url = f"https://www.komoot.de/api/v007/users/{client_id}/tours/?sport_types={sport_types}&type={type}&sort_field={sort_field}&sort_direction={sort_direction}&name={name}&status={status}&hl={hl}&page={page}&limit={limit}"

# Define the folder location and file name to save the fetched data
output_folder = "S:/Dropbox/Arbeit/05 Tableau/Databases/Komoot/JSON/"
file_name = "komoot_data.json"
file_path = f"{output_folder}{file_name}"

# define base url to retrieve information from
base_url = "https://www.komoot.de/api/v007/tours/"

# Create a session to store login information
s = requests.Session()
# Print the session object to verify
print(s)

# Perform a GET request to the login URL and store the cookies
res = requests.get(login_url)
cookies = res.cookies.get_dict()
# Print the response and cookies for debugging purposes
print(f"{res}\n{cookies}")

# Define headers for the login request
headers = {
    "Content-Type": "application/json"
}

# Prepare the payload to log in
payload = json.dumps({
    "email": email,
    "password": password,
    "reason": "null"
})

# Send a POST request to log in, using the previously obtained cookies
s.post(login_url, headers=headers, data=payload, cookies=cookies)

# Perform a GET request to another URL to complete the login process
url = "https://account.komoot.com/actions/transfer?type=signin"
s.get(url)

# Print the cookie and header information for debugging purposes
print(s.cookies.get_dict().keys())
print(dict(s.headers).keys())

# Fetch the recorded tours data using the authenticated session
response = s.get(tour_url, headers={"onlyprops": "true"})
# Check if the response status code is successful (200)
if response.status_code != 200:
    print("Something went wrong...")
    exit(1)
data = response.json()

# Write the retrieved data to a JSON file
with open(file_path, 'w') as file:
    json.dump(data, file)
print(f"Data has been saved to {file_path}")

# Prepare to fetch detailed information for each tour
for tour in data["_embedded"]["tours"]:
    tour_id = tour['id']
    tour_name = tour['name']
    # prepare the gpx files export
    gpx_url = f"{base_url}{tour_id}.gpx"  # Append ".gpx" to the URL to get the GPX file
    response = requests.get(gpx_url)
    if response.status_code == 200 or response.status_code == 304 :
        # Save the GPX data to a file
        gpx_file_path = f"{output_folder}{tour['id']}_tour_data.gpx"
        with open(gpx_file_path, 'wb') as file:
            file.write(response.content)
        print(f"GPX file for tour '{tour['id']}' | '{tour['id']}' has been downloaded and saved to '{gpx_file_path}'")
    else:
        print(f"Failed to download GPX file for tour '{tour['name']}' | '{tour['id']}' \n Status code was {response.status_code} \n")

    # prepare the JSON file export
    tourData_url = f"{base_url}{tour_id}"
    response = s.get(tourData_url, headers={"onlyprops": "true"})
    if response.status_code != 200:
        print(f"Failed to fetch data for tour {tour_id}")
        continue
    tour_data = json.loads(response.text)
    # Specify the file path where you want to save the detailed tour data
    output_file = f"{output_folder}{tour_id}_tour_data.json"
    # Write the detailed tour data to a JSON file
    with open(output_file, 'w') as file:
        json.dump(tour_data, file)
    print(f"Tour data for {tour_id} has been saved to '{output_file}'")
