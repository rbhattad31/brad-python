import numpy as np

# Create a numpy array
arr = np.array(['Andhra Pradesh', 'Telagana', 'karnataka', 'kerala'])

# Print the array
print(arr)
length_checker = np.vectorize(len)

# Find the length of each element
arr_len = length_checker(arr)

# Print the length of each element
print(arr_len)
