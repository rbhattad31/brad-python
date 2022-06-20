def fib_series(a):
    if a <= 1:
        return a

    else:
        return fib_series(a - 1) + fib_series(a - 2)


x = int(input("Enter the range number: "))

if x <= 0:
    print("Please enter a positive integer")

else:
    print("Fibonacci sequence:")

    for z in range(x):
        print(fib_series(z))
