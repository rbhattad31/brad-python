# Python code to demonstrate the working of
# sqrt() and exp()

# importing "decimal" module to use decimal functions
import decimal

# using exp() to compute the exponent of decimal number
a = decimal.Decimal(4.5).exp()

# using sqrt() to compute the square root of decimal number
b = decimal.Decimal(4.5).sqrt()

# printing the exponent
print("The exponent of decimal number is : ", end="")
print(a)

# printing the square root
print("The square root of decimal number is : ", end="")
print(b)
