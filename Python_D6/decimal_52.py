import decimal
from decimal import Decimal
ctx =decimal.getcontext()
print(ctx.prec)
print(ctx.rounding)
a = Decimal(1.25)
b = Decimal(2.4)
c = Decimal(1.8)
x = a+b+c
print(x)

print(round(a))
print(round(b))

p=Decimal((0,(2,3,5),2))
print(p)