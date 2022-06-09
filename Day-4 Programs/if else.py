#if else
a = 30
b = 20
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")
#short hand
print("short hand")
a = 30
b = 30
print("A") if a > b else print("eaual") if a == b else print("B")
#ternary operator
print("ternary operator")
a, b = 10, 20
if a != b:
	if a > b:
		print("a is greater than b")
	else:
		print("b is greater than a")
else:
	print("Both a and b are equal")

