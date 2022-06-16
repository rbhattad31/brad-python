#import complex math module

import cmath

a = float(input('enter a:'))
b = float(input('enter b:'))
c = float(input('enter c:'))

#calculation the discrimials
d =(b**2)-(4*a*c)

#find two solutions
sol1 =(-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("the solution are{0} and {1}".format(sol1,sol2))