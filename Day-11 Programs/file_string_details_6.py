
# Reading file details:
with open('sample.txt', 'r') as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split(" ")
    charc = (len(data) - len(spaces))
print("File Details::")
print("Total lines: ", len(line))
print("Total Words: ", len(words))
print("Total Spaces: ", len(spaces))
print("Total Characters: ", (len(data)-len(spaces)))
