import numpy as np
from scipy import linalg

array1 = np.array([1, 3, -2, 1])
print(array1)

#   printing dimension
print(array1.ndim)

array2 = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
array3 = np.array([2, 4, -1])

#   Passing the values to the solve function
solve = linalg.solve(array2, array3)

#   printing the result array
print(solve)
