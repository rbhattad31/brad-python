def fibonacci(n,a,b):
    if n < 0:
        return("Incorrect")
    elif n == 0 or n == 1:
        return(a)
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(b)

print("Enter the value")
n=int(input())
a=0
b=1
print(fibonacci(n,a,b))