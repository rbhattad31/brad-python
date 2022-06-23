import os

# Get current directory
path = os.getcwd()
print("Current Directory: ", path)

# parent directory
print("Parent Directory: ", os.path.abspath(os.path.join(path, os.pardir)))
