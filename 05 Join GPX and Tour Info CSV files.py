# This script is not required, as Tableau offers several possibilities to link two tables together
# Nevertheless if you need to have all data in one table, you can leverage this script to join the two tables together

import pandas as pd

# Load CSV files into pandas DataFrames
# Define the source folder
source_folder = "<your source folder>"

# Read the input CSV file
df_a = pd.read_csv(f"{source_folder}combined_data_gpx.csv")
df_b = pd.read_csv(f"{source_folder}combined_data_tour_info.csv")

# Merge DataFrames based on the common column 'Komoot Tour ID' and 'id'
merged_df = pd.merge(df_a, df_b, left_on='KomootTourID', right_on='id', how='left')

# Select the desired columns for the output
output_columns = [
    'Latitude', 'Longitude', 'Elevation', 'Timestamp', 'ActivityName', 'KomootTourID',
    'status', 'type', 'date', 'name', 'distance', 'duration', 'sport', 'elevation_up',
    'elevation_down', 'vector_map_image_src', 'map_image_src'
]
output_df = merged_df[output_columns]

# Save the result to a new CSV file
output_df.to_csv(f"{source_folder}merged_table.csv", index=False)
