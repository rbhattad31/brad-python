import numpy as np

array = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40])

print("Original array:")
print(array)

unique_elements, counts_elements = np.unique(array, return_counts=True)

print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))

rev = array[::-1]

print("Reversed array", str(rev))
