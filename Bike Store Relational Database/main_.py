import os

from b_create_database import create_database
# Create the database
create_database()

# Directory containing CSV files
current_path = os.getcwd()
directory_path = current_path + '/Bike Store Data/'

from c_read_csv_files import read_csv_files
#Read the csv_files
dataframes_list = read_csv_files(directory_path)

from d_get_file_names import get_file_names
#Get_file_names
files = get_file_names(directory_path)

# For example, print the shape of each DataFrame
for i, df in enumerate(dataframes_list):
    print(f"\n\nDataFrame {i+1} Shape: {df.shape}")
    print(f"\n\nFile {i+1} Name: {files[i]}")
    print("\n\nDatatypes:\n",df.dtypes)
    print("\n\nFirst 5 rows:\n",df.head(5))
    
from e_insert_table_into_mysql import insert_table

for i, df in enumerate(dataframes_list):
    insert_table(files[i],df)
    

#for i, file in enumerate(files):
#    print("\n\nFile:\n",file)
    
    
# Access a specific DataFrame by index
#first_dataframe = dataframes_list[0]

# Perform further analysis or manipulation on each DataFrame as needed

# To display the top 5 rows
#print("\n\nTo display the top 5 rows\n")
#print(dataframes_list[0].head(5))
    
# To display the bottom 5 rows
#print("\n\nTo display the bottom 5 rows\n")
#print(dataframes_list[0].tail(5))
    
# Checking the data type
#print("\n\nChecking the data type\n")
#print(dataframes_list[0].dtypes)
