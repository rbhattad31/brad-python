def sum_n(n):
    if n <= 1:
        return n
    else:
        return n + sum_n(n-1)

num = int(input("Enter a number: "))
print("The sum is",sum_n(num))