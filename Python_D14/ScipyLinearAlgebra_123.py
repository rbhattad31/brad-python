# Import the required libraries
from scipy import linalg
import numpy as np
x1 = int(input("Enter x1 value"))
y1 = int(input("Enter y1 value"))
x2 = int(input("Enter x2 value"))
y2 = int(input("Enter y2 value"))
p = int(input("Enter p value"))
q = int(input("Enter q value"))
# The function takes two arrays
a = np.array([[x1, y1], [x2, y2]])
b = np.array([p, q])

# Solving the linear equations
res = linalg.solve(a, b)
print(res)

# Calculating the Inverse of a Matrix
r1 = int(input("Enter r1 value"))
r2 = int(input("Enter r2 value"))
r3 = int(input("Enter r3 value"))
r4 = int(input("Enter r4 value"))
# Initializing the matrix
x = np.array([[r1, r2], [r3, r4]])

# Finding the inverse of
# matrix x
y = linalg.inv(x)
print(y)


