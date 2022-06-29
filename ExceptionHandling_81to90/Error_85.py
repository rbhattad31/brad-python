# Overflow Error
import math

try:
    print(math.exp(1000))
except OverflowError as e:
    print("overflow Error-", e)

# Reference Error

# Runtime Error
try:
    list_1 = [1, 2, 3, 4, 5, 6, 7]
    print(list_1[10])
except Exception as e:
    print("Runtime Error-", e)


# Stop Iteration


def print_n():
    for i in range(21):
        if i <= 20:
            x_1 = i
            i += 1
            print(x_1)
        else:
            raise StopIteration


print_n()
