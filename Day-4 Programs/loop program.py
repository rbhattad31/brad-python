#while loop
count = 0
while (count < 3):
    count = count + 1
    print("while loop")
#for loop
n = 10
print("for loop")
for i in range(0, n):
    if i==4:
        break
    else:
        print(i)
#continue
print("continue")
for val in "string":
    if val == "i":
        continue
    print(val)
