from decimal import *

#To view all functions in decimal module
#print(dir(decimal))
#Get context
print(getcontext())
#Get Extended context
print(ExtendedContext)
#To limit numbers using prec
num1=12.344
num2=12.344
getcontext().prec = 5
print(Decimal(num1)+Decimal(num2))
#To Round_up values
getcontext().rounding = ROUND_UP
print(Decimal('3.1415926535') + Decimal('2.7182818285'))
#Sqrt function
print(Decimal(10).sqrt())
#Exp function
print(Decimal(5).exp())
#ln function
print(Decimal(10).ln())
#Quantasize method
getcontext().rounding=ROUND_DOWN
print(Decimal('5.235466').quantize(Decimal('0.01')))
#AAbsolute function
print(Decimal(-10).__abs__())
#multiply
print(Decimal(9).__add__(Decimal(2)))
#remainder function
print(Decimal(35).remainder_near(Decimal(10)))