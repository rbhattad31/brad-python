from scipy import integrate

# Assigning square variable x for x2
square = lambda x: x**2

# Integrate the quadratic equation
Integrate = integrate.quad(square, 0, 4)

print(Integrate)

print(4**3 / 3.)
