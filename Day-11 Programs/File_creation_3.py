import os.path
import datetime
import shutil
import time
now = datetime.datetime.now()

# create multiple files[the folder sometimes not shown here check manually]
path = 'code_3_test'
path = os.path.join(os.getcwd(), path)
os.mkdir(path)
print(path)
items = ["one", "two", "three"]
file_list = []
for item in items:
    file_name = "{}{}.txt".format(item, now.strftime("%S"))
    path = os.path.join(path, file_name)
    file_1 = open(path, "w")
    file_list.append(file_name)
    path = 'code_3_test'


# Get file creation and modifications details

for file_1 in file_list:
    print("Last modified: %s" % time.ctime(os.path.getmtime(os.path.join(path, file_1))))
    print("Created: %s" % time.ctime(os.path.getctime(os.path.join(path, file_1))))

# Delete the directory
user_input = input("Enter Y or N to delete directory: ")
if user_input == 'Y':
    shutil.rmtree(path)
else:
    pass

