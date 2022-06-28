# data = data2 = ""


with open('sample2.txt') as fp:
    data = fp.read()


with open('sample1.txt') as fp:
    data2 = fp.read()


data += "\n"
data += data2

with open('sample3.txt', 'w') as fp:
    fp.write(data)
