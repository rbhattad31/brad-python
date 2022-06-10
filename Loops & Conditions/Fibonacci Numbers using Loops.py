
number = int(input("Enter Number: "))

a = 0
b = 1
sum_fib = 0
count = 1
print(a,b, end=" ")
while count <= number-2:
    sum_fib = a + b
    a = b
    b = sum_fib
    count += 1
    print(sum_fib, end=" ")