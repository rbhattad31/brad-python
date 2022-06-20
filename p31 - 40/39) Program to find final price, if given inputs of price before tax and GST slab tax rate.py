x = int(input('Price before tax: '))
y = int(input('GST slab tax rate percentage: '))

Tax_pay = float(((y / 100) * x) + x)

print('Price after GST slab tax rate is : Rs ', Tax_pay)
