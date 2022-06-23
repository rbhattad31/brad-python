
# Reading two file and paste in mew file
filenames = ['sample.txt', 'sample_1.txt']
with open('merge_file.txt', 'w') as merge_file:
    for names in filenames:
        with open(names, 'r') as fs:
            merge_file.write(fs.read())
            merge_file.write("\n")
