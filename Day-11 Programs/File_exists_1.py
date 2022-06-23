import os.path

# check file exists
print(os.path.exists('sample.txt'))

# Method-2
print(os.path.isfile('main.py'))

# check file size
size = os.path.getsize('main.py')
print("Size of the file: {} Bytes".format(size))

# File Size Method-2
f = open('main.py')
f.seek(0, os.SEEK_END)
print("Size of the file: {} Bytes".format(f.tell()))
