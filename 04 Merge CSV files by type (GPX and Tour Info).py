import os
import pandas as pd

# Define the folders
source_folder = "<your source folder>"        # Path to the CSV files directory
output_folder = f"{source_folder}alldata/"    # Path to the output directory
keywords = ["gpx", "tour_info"]               # List of specific strings in file names to look for; related to the naming in the two "Convert Komoot... .py" scripts

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created output directory: {directory}")

def append_csv_files(source_folder, output_folder, keyword):
    # Get a list of all files in the source folder
    all_files = os.listdir(source_folder)
    
    # Filter out non-CSV files and files that do not contain the keyword
    csv_files = [file for file in all_files if file.endswith(".csv") and keyword in file]
    
    if not csv_files:
        print(f"No matching CSV files found for keyword: {keyword}")
        return
    
    # Initialize an empty list to hold DataFrames
    data_frames = []
    
    # Loop through the CSV files and read their data into DataFrames
    for csv_file in csv_files:
        csv_path = os.path.join(source_folder, csv_file)
        df = pd.read_csv(csv_path)
        data_frames.append(df)
        print(f"Read data from {csv_path}")
    
    # Concatenate the DataFrames in the list along rows
    combined_data = pd.concat(data_frames, ignore_index=True)
    
    # Create the output folder if it doesn't exist
    ensure_directory(output_folder)
    
    # Write the combined data to the output CSV file
    output_file = os.path.join(output_folder, f"combined_data_{keyword.replace('.', '_')}.csv")
    combined_data.to_csv(output_file, index=False)
    print(f"Combined data for keyword {keyword} written to {output_file}")

if __name__ == "__main__":
    for keyword in keywords:
        append_csv_files(source_folder, output_folder, keyword)
