import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

# Sum all the elements of each column of the array
sum_of_array = np.sum(array, axis=0)

# Output the array
print(array)

print("\n")

# Output the sum
print("", sum_of_array, "is the sum of the all the columns of the above matrix")
