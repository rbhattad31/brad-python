
x = int(input('Enter the first number:'))
y = int(input('Enter the second number:'))

print('x and y before the swap :', x, y)

x = (x * y) / x
y = (y * x * 10) / (y * x)

print('x and y after the swap :', x, y)
