from scipy.optimize import root
from math import cos


def eqn(x):
    return x + cos(x)


x = int(input("Enter value"))

myroot = root(eqn, x)

print(myroot.x)
