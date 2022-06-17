import decimal

# return decimal value
print(decimal.Decimal(25.36))
# return square root value
print(decimal.Decimal(3.5).sqrt())
# return exponential value
print(decimal.Decimal(2.5).exp())
# return log value
print(decimal.Decimal(4.5).log10())
# Show decimal as tuple
print(decimal.Decimal(27.5).as_tuple())
# Perform Fused Multiply and Add
print(decimal.Decimal().fma(4,9))
# return compare values
# #Compare when both are equal
print('Compare value: ' + str(decimal.Decimal(-0.1).compare(decimal.Decimal(-0.1))))
# Compare when first one is smaller
print('Compare value: ' + str(decimal.Decimal(-1.3).compare(decimal.Decimal(2.26))))
# Compare when first one is greater
print('Compare value: ' + str(decimal.Decimal(-5.3).compare(decimal.Decimal(-7.25))))
