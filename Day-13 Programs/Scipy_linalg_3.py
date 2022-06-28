from scipy import linalg
import numpy as np

# Solve linear equations
l2 = np.array([[8, 2], [4, 7]])
l1 = np.array([12, 10])
linear_equation = linalg.solve(l2, l1)
print('Linear Equation\n', linear_equation)

# Inverse of matrix
arr = np.array([[8, 2], [4, 7]])
inv_arr = linalg.inv(arr)
print('Inverse array\n', inv_arr)

# Determinant of matrix
deter_val = linalg.det(arr)
print('Determinant\n', deter_val)

# Singular value decomposition
x, y, z = linalg.svd(arr)
print('Singular value decomposition')
print(x, y, z)

# Eigen value & vector
val, vect = linalg.eig(arr)
print('Eigen Value:\n', val)
print('Eigen Vector:\n', vect)

# Calculate norm
# Calculating the L2 norm
l2 = linalg.norm(arr)
# Calculating the L1 norm
l1 = linalg.norm(arr, 1)
print('L2 norm\n', l2)
print('L1 norm\n', l1)
