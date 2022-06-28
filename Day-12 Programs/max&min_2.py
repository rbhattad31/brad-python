import numpy as np

arr_1 = np.matrix([[0.5, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]])
print("Matrix:\n", arr_1)

# Get number of rows.
print("Rows:", np. size(arr_1, 0))

# Get number of columns.
print("Columns:", np. size(arr_1, 1))

# Maximum element:
print("Maximum Element:", np.max(arr_1))

# Minimum element:
print("Maximum Element:", np.min(arr_1))
