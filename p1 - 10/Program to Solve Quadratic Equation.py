import cmath

a = int(input('Enter the numerical coefficient of square variable:'))
b = int(input('Enter the numerical coefficient of next variable:'))
c = int(input('Enter the value of the constant:'))

d = cmath.sqrt((b * b) - (4*a*c))

e = ((- b + d) / 2 * a)
f = ((- b - d) / 2 * a)

print('The first value of the quadratic equation is :', e)
print('The first value of the quadratic equation is :', f)
