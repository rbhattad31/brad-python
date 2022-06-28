from scipy.integrate import *
from numpy import *

# General Integration
integrate_val = quad(lambda x: exp(-x**2), 0, 1)
print("General integration")
print(integrate_val)

# Double integration
double_integration = dblquad(lambda x, y: x * y, 0, 0.5, lambda x: 0, lambda x: 1 - 2 * x)
print("Double integration")
print(double_integration)

# Multiple integration
multiple_integration = nquad(lambda x, y, z: x * y * z, [[0, 1], [2, 5], [3, 5]])
print("Multiple integration")
print(multiple_integration)

# Fixed order Integration
gauss_order = fixed_quad(lambda x: 3 * x ** 3, 1.0, 2.0, n=2)
print("Fixed order integration")
print(gauss_order)

# Fixed tolerance gaussian quadrature
gauss_quadrature = quadrature(lambda x: 3 * x ** 3, 0.0, 1.0)
print("Gauss quadrature integration")
print(gauss_quadrature)

# Rom-berg function
rom_berg_function = romberg(lambda x: 3 * pi * x ** 3, 1, 2, show=True)
print("Rom-berg integration")
print(rom_berg_function)

# Cumtraz function
a = arange(0, 5)
b = arange(0, 5)
print("Cumtraz method")
print(cumtrapz(b, a))

# Simps method
print("Simps method")
print(simps(b, a))

# Romb method
print("Romb method")
print(romb(b))
