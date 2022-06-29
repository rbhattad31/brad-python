# Example-1

try:
    raise ValueError('The value error exception', 'x', 'y')
except ValueError as ex:
    print(ex)

# Example-2
try:
    print(6 / 0)
except ZeroDivisionError as ex:
    raise ValueError('b must not zero')

# Example-3[Try 2 or 3 at one time]
try:
    raise NameError("Hi")
except NameError:
    print("An exception")
    raise
