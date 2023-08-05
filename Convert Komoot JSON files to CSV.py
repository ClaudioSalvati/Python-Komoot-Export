# Import necessary libraries
import json
import pandas as pd
import os
import re

# Define the input folder where the JSON files are located
input_folder = "<your input folder>"
# Define the output folder where the CSV files will be saved
output_folder = "<your output folder>"

# Function to sanitize the name and replace forbidden characters with "_"
# In case you have used characters in the tours name that are forbidden in file names (I did)
def sanitize_name(name):
    return re.sub(r'[\\/:*?"<>|]', '_', name)

# Get a list of all JSON files in the input folder
json_files = [file for file in os.listdir(input_folder) if file.endswith(".json")]

# Iterate through each JSON file
for json_file in json_files:
    # Skip the file if it has the name "komoot_data.json"
    # this file is generated in the script "Get Komoot tour JSON data.py" and should be converted to CSV. I stored it in the same folder and needed to skip it
    if json_file == "komoot_data.json":
        continue

    # Read the JSON data into a DataFrame using Pandas
    df = pd.read_json(os.path.join(input_folder, json_file))

    # Select only the desired columns from the DataFrame and make a copy
    selected_columns = ["status", "type", "date", "name", "distance", "duration", "sport", "elevation_up", "elevation_down", "id"]
    df_selected = df[selected_columns].copy()

    # Convert the "date" column to datetime format and then to string to extract the first 10 characters - YYYY-MM-DD
    df_selected["activity_date"] = pd.to_datetime(df_selected["date"]).dt.strftime("%Y-%m-%d").str[:10]

    # Extract additional data from the JSON using .loc to add two new columns: "vector_map_image_src" and "map_image_src"
    df_selected.loc[:, "vector_map_image_src"] = df["vector_map_image"]["src"]
    df_selected.loc[:, "map_image_src"] = df["map_image"]["src"]

    # Create a new DataFrame without duplicate rows
    df_selected_unique = df_selected.drop_duplicates()

    # Convert the "vector_map_image_src" column to string type using .loc
    df_selected_unique.loc[:, "vector_map_image_src"] = df_selected_unique["vector_map_image_src"].astype(str)
    
    # Replace "{width}" and "{height}" with "1920" in the "vector_map_image_src" column using .loc
    df_selected_unique.loc[:, "vector_map_image_src"] = df_selected_unique["vector_map_image_src"].str.replace("{width}", "1920").str.replace("{height}", "1920")

    # Define the output CSV filename based on the activity date and name
    activity_date = df_selected_unique["activity_date"].iloc[0]
    name = df_selected_unique["name"].iloc[0]

    # Sanitize the name to replace any forbidden characters with "_"
    name = sanitize_name(name)

    csv_file = f"{output_folder}{activity_date}_{name}_tour_info.csv"

    # Save the table to the CSV file without row indexes
    df_selected_unique.to_csv(os.path.join(input_folder, csv_file), index=False)

    # Print a message indicating that the table has been saved as a CSV file
    print(f"Table has been created and saved as '{csv_file}'.")
