# Python program to explain shutil.copytree() method


# importing shutil module
import shutil

# path
path = 'kumar.txt'

# Source path
src = 'kumar.txt'

# Destination path
dest = 'kumar.txt'

# Copy the content of
# source to destination
destination = shutil.copytree(src, dest)

# print(destination) prints the
# path of newly created file