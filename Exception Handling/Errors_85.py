# Overflow Error
import math

try:
    print(math.exp(100))
except OverflowError as e:
    print("overflow Error-", e)



# Runtime Error
try:
    x = 1
    y = 0
    print("Result", x/y)
except Exception as e:
    print("Runtime Error-", e)


# Stop Iteration


def print_n():
    for i in range(m):
        if i <= 10:
            x_1 = i
            i += 1
            print(x_1)
        else:
            raise StopIteration

m = 20
print_n()