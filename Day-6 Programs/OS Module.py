import os

current_dir = os.getcwd()
print("Working directory:\n", current_dir)
# Change Directory
os.chdir('../')
print("Working directory after change:\n", os.getcwd())
# create directory
new_dir = "Demo_Dir"
path = os.path.join(current_dir, new_dir)
os.mkdir(path)
print("Directory '% s' created" % new_dir)
# List files
file_list = os.listdir(current_dir)
print("Files and directories in current path")
print(file_list)
# Remove directory
os.rmdir(path)
print("Directory '% s' removed" % new_dir)

# Remove directory or file[create sample file for testing]
# new_dir = "file1.txt"
# path = os.path.join(current_dir, new_dir)
# os.remove(path)
# print("Directory '% s' removed" % new_dir)

# os name
print(os.name)

# check path exists
filename = 'OS Module.py'
path = os.path.join(current_dir, filename)
result = os.path.exists(path)
print(result)
# Get size
print(os.path.getsize(path), 'bytes')
