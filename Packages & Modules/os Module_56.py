import os

# Shows all the methods we access in this module
print(dir(os))

# return current working directory
print(os.getcwd())

# changes the directory
os.chdir('/Users/HP')
# creates directory and sub-dir
os.mkdir('Music-7')
# remove directory
os.removedirs('Music-4')
# rename directory
os.rename('Music-7','Music-4')


# return files or folders in current directory
print(os.listdir())