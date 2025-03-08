import shutil
import os
import time
import json

#Loads configuration
with open("config.json", "r") as file:
    category_dict = json.load(file)

file_list = []
other_files = []

#Shows loaded configuration
print(f"Current configuration:\n{json.dumps(category_dict, indent=4)}")

#Establish working directory
cdw = input("Which directory to sort? (Skip for current): ")
if cdw == "":
    cdw = os.getcwd()

#Main loop
while True:
    #Scans working direcotry for files, adds to list
    direc = os.scandir(cdw)
    for entry in direc:
        if entry.is_file():
            if entry.name not in file_list:
                print(f"File detected: {entry.name}")
                file_list.append(entry.name)

    #Sorting loop
    #Starts by isolating file extension from file 
    for file in file_list[:]: #Shallow copy for safer iterations
        sort = False
        file_path = os.path.join(cdw, file)
        start = file.rfind(".")
        file_type = file.split(".")[-1]
        
        #Compares file type to categories
        for category, extensions in category_dict.items():
            #If the file is assigned in the config, sorts to directory
            if file_type in extensions:
                dest_folder = os.path.join(cdw, category)
                dest_path = os.path.join(dest_folder, file)
                os.makedirs(dest_folder, exist_ok=True)
                if file == os.path.basename(__file__):
                    continue
                else:
                    shutil.move(file_path, dest_path)
                    print(f"Moved {file} to {dest_path}")
                file_list.remove(file)
                sort = True
                break
        #If file is not assigned, adds to list
        if not sort and file not in other_files:
            other_files.append(file)
    #Prints list of unsorted files
    if other_files:
        print("\nFollwoing files have no assigned category in configuration:")
        for other in other_files:
            print(f"- {other}")    

    print("Sleeping for 3 seconds")
    time.sleep(3)