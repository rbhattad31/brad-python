# Handling it manually
try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)

# the errror_message provided by the user gets printed
except AssertionError as msg:
    print(msg)


# Python program to demonstrate
# AttributeError


class Geeks():

    def __init__(self):
        self.a = 'hello world'


# Driver's code
obj = Geeks()

print(obj.a)

# Raises an AttributeError as there
# is no attribute b
print(obj.b)


# Python program to demonstrate
# AttributeError


class Geeks():

    def __init__(self):
        self.a = 'GeeksforGeeks'


# Driver's code
obj = Geeks()

print(obj.a)

# Raises an AttributeError as there
# is no attribute b
print(obj.b)