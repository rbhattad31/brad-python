from scipy import linalg
import numpy as np

# The function takes two arrays
a = np.array([[7, 2], [4, 5]])
b = np.array([8, 10])

# Solving the linear equations
res = linalg.solve(a, b)
print(res)

# Initializing the matrix
x = np.array([[7, 2], [4, 5]])

# Finding the inverse of
# matrix x
y = linalg.inv(x)
print(y)
x = np.array([[8, 2], [3, 5], [1, 3]])

# finding the pseudo inverse of matrix x
y = linalg.pinv(x)
print(y)
A = np.array([[9, 6], [4, 5]])

# Finding the determinant of matrix A
D = linalg.det(A)
print(D)
M = np.array([[1, 5], [6, 10]])

# Passing the values to the
# eigen function
x, y, z = linalg.svd(M)
print(x, y, z)