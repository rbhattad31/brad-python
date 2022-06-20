a = 100
b = 50
if b > a:
    print("b is greater than a")
    if a > b:
        print("a is greater than b")
    elif a == b:
        print("a is greater than b")
else:
    print("a is not equal to b")

if a > b: print("a is greater than b")

print("A") if a > b else print("B")
