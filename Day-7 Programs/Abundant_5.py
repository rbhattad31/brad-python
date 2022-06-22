import math


def sum_div(n):
    val = 0
    i = 1
    while i <= (math.sqrt(n)):
        if n % i == 0:
            if n // i == i:
                val = val + i
            else:  # Otherwise take both
                val = val + i
                val = val + (n // i)
        i = i + 1
    val = val - n
    return val


def check_abundant(n):
    if sum_div(n) > n:
        return 'yes, the number is abundant'
    else:
        return 'No, the number is not abundant'


num = int(input("Enter the input: "))
print(check_abundant(num))
