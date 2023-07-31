# Convert Komoot GPX files to CSV

# load libraries
import gpxpy
import csv
import os

# define the folders
input_folder = "<your input folder>"
output_folder = "<your output folder>"

def get_activity_info(gpx):
    # Extract activity name from GPX file, if available
    activity_name = gpx.name or ""

    return activity_name

def gpx_to_csv(input_file, output_folder):
    with open(input_file, 'r', encoding='utf-8') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Get activity information
    activity_name = get_activity_info(gpx)

    # Get the activity date from the first point's time
    activity_date = gpx.tracks[0].segments[0].points[0].time.strftime("%Y-%m-%d")

    # Extract the data from the GPX file
    data = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                data.append([point.latitude, point.longitude, point.elevation, point.time])

    # Remove 14 characters from the rightmost side of the original GPX file name
    original_gpx_file_name = os.path.basename(input_file)[:-14]

    # Write the data to a CSV file
    output_filename = f"{activity_date}_{activity_name}.csv" if activity_name else f"{original_gpx_file_name}.csv"
    output_file = os.path.join(output_folder, output_filename)
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header
        writer.writerow(["Latitude", "Longitude", "Elevation", "Timestamp", "ActivityName", "KomootTourID"])

        # Write the data rows
        for row in data:
            writer.writerow(row + [activity_name, original_gpx_file_name])

    print(f"CSV file '{output_file}' created successfully.")

def batch_convert_gpx_to_csv(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all GPX files in the input folder
    gpx_files = [file for file in os.listdir(input_folder) if file.endswith('.gpx')]

    # Loop through each GPX file and convert it to CSV
    for gpx_file in gpx_files:
        input_path = os.path.join(input_folder, gpx_file)
        gpx_to_csv(input_path, output_folder)

    print("Batch conversion completed.")

# Usage example
if __name__ == "__main__":
    batch_convert_gpx_to_csv(input_folder, output_folder)
