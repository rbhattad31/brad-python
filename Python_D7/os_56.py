import os
from datetime import datetime
print(dir(os))

# to get current working directory
print(os.getcwd())

# to print the list of files in the directory
print(os.listdir())

# to create new file in the directory
# os.mkdir('Sys_57.py')
print(os.listdir())

# renaming the file

# os.rename('Os_56.py','os_56.py')
# print(os.listdir())

# to get the file details and modified date
print(os.stat('os_56.py'))
print(os.stat('os_56.py').st_size)
mod_time = os.stat('os_56.py').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('/Users\saian\OneDrive/Desktop'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

# to get Environment variables
print(os.environ.get('HOME'))
