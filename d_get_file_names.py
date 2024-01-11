import os

def get_file_names(directory_path):
    print("\n\Get file names\n\n")
    # Directory containing CSV files
    #current_path = os.getcwd()
    #directory_path = current_path + '/Bike Store Data/'
    print("Current Working Directory: ",directory_path)
    # List all files in the directory
    lst = os.listdir(directory_path)
    files = []
    for x in lst:
        files.append(os.path.splitext(x)[0])
        #os.path.splitext(x)[0]
    
    print("Files: ",files)
    return files
