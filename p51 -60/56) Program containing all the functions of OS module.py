import os

# To get current directory
cwd = os.getcwd()

print("Current working directory:", cwd)


# To change current working directory
os.chdir('../')

# To join path
directory = "New_Python"
parent_dir = "D:"
path = os.path.join(parent_dir, directory)
print(path)

# To create directory
os.mkdir(path)

# To create directory with mode
mode = 0o666
directory1 = "New_Python"
parent_dir1 = "E:"
path1 = os.path.join(parent_dir1, directory1)
os.mkdir(path1, mode)

# To create a directory recursively
directory2 = "New_Python"
parent_dir2 = "F"
path2 = os.path.join(parent_dir2, directory2)
os.makedirs(path2, mode)

dir_list = os.listdir(path)
print(dir_list)

# To remove or delete a file path
os.remove(path)

# To remove or delete an empty directory
os.rmdir(path)

# To print operating system dependent module imported
print(os.name)

result = os.path.exists("test.csv")

print(result)
