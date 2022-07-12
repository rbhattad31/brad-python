#write a program to find the number of rows and columns of a matrix using NumPy and get maximum and minimum values of the matrix
import numpy as np

matrix = np.arange(0, 9).reshape((3, 3))

# Original matrix
print(matrix)

# Number of rows and columns of the said matrix
print(matrix.shape)