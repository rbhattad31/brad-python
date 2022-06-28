import os
import datetime

directory = 'Created'
parent_dir = 'C:\Python_D12'
path = os.path.join(parent_dir, directory)
os.mkdir(path)

# creating new files
file1 = open("Created/Three.txt", "a")  # append mode
file1.write(
    "When the file is opened in append mode, the handle is positioned at the end of the file. The data being written "
    "will be inserted at the end, after the existing data. Let’s see the below example to clarify the difference "
    "between write mode and append mode.")
file1.close()

# Get creation and modification date
file_path = "C:\Python_D12\Created/Three.txt"
c_time = os.path.getctime(file_path)
m_time = os.path.getmtime(file_path)

print("File created at =>", datetime.datetime.fromtimestamp(c_time))
print("File modified at =>", datetime.datetime.fromtimestamp(m_time))

# Files count
dir_path = "C:\Python_D12\Created"

count = 0
# Iterate directory
for path in os.listdir(dir_path):

    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)


# delete files
del_file = "C:\Python_D12\Created/One.txt"
os.remove(del_file)

# delete folder

del_folder = "C:\Python_D12\Created"
os.rmdir(del_folder)
