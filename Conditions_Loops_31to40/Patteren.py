size = 5
count = 0

for i in range(size):
    if i>=1:
        for j in range(i):
            print(chr(65 + count), end=" ")
            count += 1
        print()