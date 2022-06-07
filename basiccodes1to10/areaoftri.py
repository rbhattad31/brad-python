a = float(input('side1 '))
b = float(input('side2 '))
c = float(input('side3 '))

x = (a+b+c)/2

area = (x*(x-a)*(x-b)*(x-c)) * 0.5
print('area of triangle is ', area)