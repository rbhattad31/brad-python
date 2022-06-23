def count_file(file_1):
    with open(file_1) as f_1:
        for j, l in enumerate(f_1):
            pass
    return j + 1


print("Number of lines in the file: ", count_file("sample.txt"))

# search for a string
words = ['you', 'audio']
with open(r'sample.txt', 'r') as f:
    for word in words:
        for i, line in enumerate(f):
            if word in line:
                print('string found in a line {} : \n{}'.format(i, line))
                break  # if you want to search multiple places remove break
            else:
                pass
