#write a program to append the data entered by user using input() to a text file
# Python program to
# demonstrate merging
# of two files

data = data2 = ""

# Reading data from file1
with open('kumar.txt') as fp:
    data = fp.read()

# Reading data from file2
with open('vinay.txt') as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open('aa.txt', 'w') as fp:
    fp.write(data)