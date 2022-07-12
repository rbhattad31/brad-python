#write a program to demonstrate Integration with Scipy – Numerical Integration functions scipy.integrate library
import scipy.integrate as integrate
import scipy.special as special
result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
print(result)