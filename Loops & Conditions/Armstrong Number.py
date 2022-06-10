n=input()
a=len(n)
s=0
for i in n:
    s=s+int(i)**a
if s == int(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")