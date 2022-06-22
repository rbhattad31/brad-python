# AssertionError
try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)
except AssertionError:
    print("AssertionError")

# Attribute Error
try:
    X = 100
    X.append(9)
except Exception as message:
    print(message)

# EOF Error[if you want to test this case remove last  parenthesis from print]
name = "Vanilla Shortbread"
author = "Career Karma"
vegetarian = "This recipe is vegetarian."
print("The {} recipe was devised by {}. {}".format(name, author, vegetarian))

# Floating point error
val = 0.1 + 0.2
# with error
print(val)
# without error
print(f"val = {val:.2f}")
