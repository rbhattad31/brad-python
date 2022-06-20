n = int(input("Enter the range number:"))

i = 0
j = 1
k = 0

if n <= i:
    print("Nil")
elif n == j:
    print("The numbers are:", i)
else:
    print("Fibonacci sequence:")
    while k < n:
        print(i)
        c = i + j
        i = j
        j = c
        k = k + 1
