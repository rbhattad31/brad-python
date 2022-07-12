#write a program to extract data from an archive with .zip extension folder
# importing required modules
from zipfile import ZipFile

# specifying the zip file name
file_name = "kk.zip"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')