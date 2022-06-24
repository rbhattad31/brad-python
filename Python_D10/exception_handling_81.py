try:
    a = int(input("Enter the a value:"))
    b = int(input("Enter the b value:"))
    c = a/b
except ZeroDivisionError:
    print("Denominator should not be 0")
else:
    print("The value of c is:", c)
finally:
    print("Happy learning")
