import numpy as np

# Create a numpy array
arr = np.array(['Tim', 'Alan', 'Clinton', 'Vikram'])

# Print the array
print(arr)

# Use vectorize function of numpy
length_checker = np.vectorize(len)

# Find the length of each element
arr_len = length_checker(arr)

# Print the length of each element
print(arr_len)


output = np.char.swapcase(arr)
print("The output swap cased array :")
print(output)
