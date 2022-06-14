# Pass by Value
def hello(x):
    x = 45
    print(x)
    return


x = 13
hello(x)
print(x)

# Pass by Reference
a = [1, 2, 3, 4]


def myfun(i):
    i[0] = 18
    print(i)
    return


myfun(a)
print(a)

# anonymous Function
p = int(input("Enter your first value"))
q = int(input("Enter your second value"))
sum = lambda p, q: p+q
print("The sum is",sum(p,q))
