import os

path = 'check_file.txt'

isFile = os.path.isfile(path)

print(isFile)

#   checking if the file exists
if isFile:

    size = os.path.getsize(path)
    print(f'The {path} size is', size, 'bytes')
