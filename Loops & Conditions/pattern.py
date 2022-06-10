num = 5
counter = 0

for i in range(num):
    if i>=1:
        for j in range(i):
            print(chr(65 + counter), end=" ")
            counter = counter + 1

        print()