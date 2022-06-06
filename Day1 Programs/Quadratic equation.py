import cmath

a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))
d = (b**2) - (4*a*c)
sol_1 = (-b-cmath.sqrt(d))/(2*a)
sol_2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol_1,sol_2))