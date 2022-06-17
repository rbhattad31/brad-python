# Qudratic equation
import cmath
print("General_equation(a*x**2+b*x+c)")
a = int(input("Enter the value of a (a != 0) = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))

d= ((b**2)-(4*a*c))**0.5
Sol1 = (-b+cmath.sqrt(d))/(2*a)
Sol2 = (-b-cmath.sqrt(d))/(2*a)

print("The solution are {} and {} ".format(Sol1,Sol2))