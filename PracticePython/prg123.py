#write a program to demonstrate Linear Algebra functions with SciPy.linalg
from scipy import linalg
import numpy as np

# The function takes two arrays
a = np.array([[7, 2], [4, 5]])
b = np.array([8, 10])

# Solving the linear equations
res = linalg.solve(a, b)
print(res)