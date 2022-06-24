import os
import zipfile

# Getting current directory
dir_name = os.getcwd()
extension = ".zip"

# change directory from working dir to dir with files
os.chdir(dir_name)

# Loop through items in dir
for item in os.listdir(dir_name):
    if item.endswith(extension):
        with zipfile.ZipFile(item, 'r') as z:
            z.printdir()
            print('Extracting all the files now...')
            z.extractall()
            print('Done!')