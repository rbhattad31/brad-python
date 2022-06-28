import numpy as np

# create 1d-array
arr = np.arange(36)

# reshape to 2d-array
arr_1 = np.reshape(arr, [4, 9])
print("Original array:")
print(arr_1)

# calculate sum of columns
sum_col = arr_1.sum(axis=0)
print()
print("Sum of all columns:")
print(sum_col)
