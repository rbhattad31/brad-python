number = 5
is_divisible_by_10 = (number % 10 == 0)
is_divisible_by_5 = (number % 5 == 0)
if is_divisible_by_10:
	print("Divisible by 10")
elif is_divisible_by_5:
	print("Divisible by 5")
else:
	print("Not Divisible by 10 or 5")

# short hand
print("short hand")
a = int(input())
b = int(input())
print("A") if a > b else print("equal") if a == b else print("B")
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