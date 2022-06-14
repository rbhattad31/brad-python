def sum(x, y):
    if (y == 0):
        return x;
    else:
        return (1 + sum(x, y - 1));


x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
print("Sum of two numbers are: ", sum(x, y))