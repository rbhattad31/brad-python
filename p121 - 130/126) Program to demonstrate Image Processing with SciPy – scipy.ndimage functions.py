from scipy import ndimage
import numpy as np

array1 = np.array([[1, 2, 0, 0], [5, 3, 0, 4], [0, 0, 0, 7], [9, 3, 0, 0]])

array2 = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 0]])

# Multidimensional convolution of the array with the given kernel
result1 = ndimage.convolve(array1, array2, mode='constant', cval=0.0)

print(result1)

array3 = np.array(([0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]))

# To calculate the center of mass of the values of an array
result2 = ndimage.center_of_mass(array3)

print(result2)
