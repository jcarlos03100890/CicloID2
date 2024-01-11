import os
import pandas as pd

def read_csv_files(directory_path):
    print("\n\nReading files\n\n")
    # Directory containing CSV files
    #current_path = os.getcwd()
    #directory_path = current_path + '/Bike Store Data/'
    print("Current Working Directory: ",directory_path)
    # List all files in the directory
    files = os.listdir(directory_path)
    print("Files: ",files)
    # Filter only CSV files
    csv_files = [file for file in files if file.endswith('.csv')]

    # Create an empty list to store DataFrames
    dataframes_list = []

    # Loop through each CSV file and read into DataFrame
    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        df = pd.read_csv(file_path)
    
        # You can perform additional processing or analysis on each DataFrame if needed
    
        # Append the current DataFrame to the list
        dataframes_list.append(df)

    # Now, dataframes_list contains all DataFrames from the CSV files in the directory
    # You can manipulate each DataFrame separately in the list
    return dataframes_list
    
    
