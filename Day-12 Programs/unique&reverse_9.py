import numpy as np

# Get unique values & index location from a numpy array
arr = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18])
print('Original numpy array : ', arr)
uniqueValues, indicesList = np.unique(arr, return_index=True)
print('Unique Values : ', uniqueValues)
print('Indices of unique Values : ', indicesList)

# Reverse array using flipud method
rev_arr = np.flipud(arr)
print("Reverse array: ", rev_arr)
