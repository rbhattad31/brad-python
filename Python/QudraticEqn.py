
import cmath

a = 2
b = 7
c = 12

#
# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

print(type(sol1))