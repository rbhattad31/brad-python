import numpy as np
a = np.array([10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40, 35, 35, 25,20 ])
print("Original array:", a)
unique_elements, counts_elements = np.unique(a, return_counts=True)
print("Frequency of unique values of the array:", np.asarray((unique_elements, counts_elements)))
