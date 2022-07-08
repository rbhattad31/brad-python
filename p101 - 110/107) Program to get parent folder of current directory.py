# Python program to get parent
# directory


import os

# get current directory
path = os.getcwd()
print("Current directory", path)

path1 = os.pardir

# prints parent directory
print("Parent directory", os.path.abspath(os.path.join(path, os.pardir)))
