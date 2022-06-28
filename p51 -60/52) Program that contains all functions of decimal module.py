import decimal

my_dec = decimal.Decimal(25.36)
print(my_dec)
print('Square Root is: ' + str(my_dec.sqrt()))
print('e^x is: ' + str(my_dec.exp()))
print('ln(x) is: ' + str(my_dec.ln()))
print('log(x) is: ' + str(my_dec.log10()))

my_dec1 = decimal.Decimal(5.3)
print(my_dec1)
my_dec2 = decimal.Decimal(-9.23)
print(my_dec2)

print('\nMy_dec1 as tuple: ' + str(my_dec1.as_tuple()))
print('\nMy_dec2 as tuple: ' + str(my_dec2.as_tuple()))

#   Perform Fused Multiply and Add

print('\n(x*5)+8 is: ' + str(my_dec1.fma(5, 8)))

print('Minimum: ' + str(my_dec1.min(my_dec2)))
print('Maximum: ' + str(my_dec2.max(my_dec1)))


print('Compare value: ' + str(decimal.Decimal(-5.3).compare(decimal.Decimal(9.26))))

#   Copy values

my_dec = decimal.Decimal(-25.36)
print(my_dec)

temp_dec = my_dec.copy_abs()

print('Absolute value is: ' + str(temp_dec))

my_dec = decimal.Decimal(7.26)
temp_dec = my_dec.copy_negate()
print('Negative of 7.26 is: ' + str(temp_dec))

my_dec = decimal.Decimal(-25.36)
temp_dec = my_dec.copy_sign(decimal.Decimal(12.5))
print('Copy sign from second argument: ' + str(temp_dec))
