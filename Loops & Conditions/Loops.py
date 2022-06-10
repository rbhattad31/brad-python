a = int(input())
counter = 0
while counter < 3:
    a = a + 1
    print(a)
    counter = counter + 1
#for loop
n = 30
for i in range(0, n):
    if i==5:
        break
    else:
        print(i)
#continue

for val in "string":
    if val == "i":
        continue
    print(val)