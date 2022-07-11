# quad – General Purpose Integration
from scipy.integrate import dblquad
from scipy.integrate import quad
from scipy.integrate import nquad
from scipy import integrate
import numpy as np


def f(x):
    return 3.0 * x * x + 1.0


I, err = quad(f, 5, 7)
print(I)
print(err)
# dblquad :General Purpose Double Integration

area = dblquad(lambda x, y: x * y, 0, 0.5, lambda x: 0, lambda x: 1 - 2 * x)

print("dblquad", area)


# nquad – General Purpose n- fold Integration

def f(x, y, z):
    return x * y * z


N = nquad(f, [[0, 1], [0, 5], [0, 5]])
print("nquad", N)


# fixed_quad :computation of a definite integral
def func(x): return 3 * x ** 3


# n is the order of integration
p = integrate.fixed_quad(func, 1.0, 2.0, n=2)

print("fixed_quad", p)


# quadrature :computation of definite integral using fixed tolerance gaussian quadrature
# import scipy.integrate.


def f(x): return 3 * x ** 3


# using scipy.integrate.quadrature() method
g = integrate.quadrature(f, 0.0, 1.0)

print("quadrature", g)

# romberg :
# import numpy and scipy.integrate
f = lambda x: 3 * np.pi * x ** 3

# using scipy.integrate.romberg()
r = integrate.romberg(f, 1, 2, show=True)

print("romberg", r)

# trapz :

b = [1, 19]
a = [1, 9]

t = np.trapz(b, a)

print(t)

