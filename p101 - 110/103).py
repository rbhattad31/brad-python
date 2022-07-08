# Write a python code to create few files in a new folder then count, Get File Creation and Modification DateTime and
# display all the files in a directory/folder, after verification delete all files and delete the folder using code


import os
from datetime import datetime

fp = open('New/sales.txt', 'x')
fp.close()
fp = open('New/sales1.txt', 'x')
fp.close()

# Assigning directory path
dir_path = r'New'

# Assigning empty array object to store the files in the directory
res = []

for path in os.listdir(dir_path):

    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

print(res)

# Getting file modification time as timestamp value
y = os.path.getmtime('New/sales1.txt')

# Getting file creation timestamp value
x = os.path.getctime('New/sales1.txt')

print(x)
print(y)


# Convert to datetime from timestamp values x and y

dt = datetime.fromtimestamp(x)
print("The modification date and time is:", dt)

dt1 = datetime.fromtimestamp(y)
print("The creation date and time is:", dt1)

# Deleting the files created

os.remove("New/sales.txt")
os.remove("New/sales1.txt")


for f in os.listdir(dir_path):
    os.remove(os.path.join(dir_path, f))

print("Files deleted successfully")
