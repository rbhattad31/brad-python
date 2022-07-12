#write a program to find number of characters, words, spaces and lines in a file

file_IO = open('kumar.txt')
with open('kumar.txt','r')as f:
    data = f.read()
    line = data.splitlines()
    words = data.split()
    spaces = data.split()
    charc = (len(data)-len(spaces))
print('\n Line number ::', len(line), '\n Words number ::', len(words), '\n Spaces ::', len(spaces), '\n Characters ::', (len(data)-len(spaces)))