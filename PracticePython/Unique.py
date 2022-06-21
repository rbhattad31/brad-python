x = [3, 2, 4, 5, 2, 8, 9, 4]
print("Input list : ", x)

y = []
count = 0

for i in x:
    if i not in y:
        count = count + 1
        y.append(i)

print("Output list : ", y)
print("No. of unique items are:", count)


