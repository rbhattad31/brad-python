# Opening a file
file = open("count.txt", "r")
Counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1
print(Counter)

words = ['Today', 'is']
with open(r'count.txt', 'r') as f:
    for word in words:
        for i, line in enumerate(f):
            if word in line:
                print('string found in a line {} : \n{}'.format(i, line))
                break  # if you want to search multiple places remove break
            else:
                pass
