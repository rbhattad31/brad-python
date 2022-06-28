file = open("sample2.txt", "r")
Counter = 0
flag = 0
Content = file.read()

CoList = Content.split("\n")
string1 = 'Indicant pueri'
for i in CoList:
    if i:
        Counter += 1
        if string1 in CoList:
            flag = 1
            break
if flag == 0:
    print('String', string1, 'Not Found')
else:
    print('String', string1, 'Found In Line', Counter)

print(Counter)
