a=0
b=1
print("Enter the value")
n=int(input())
if n<0:
    print("Incorrect")
elif n==0 or n==1:
    print(a)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(b)