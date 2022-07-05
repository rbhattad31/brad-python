import numpy as np
a = np.array([2, 3, 4, 5, 8, 5, 9])
print(np.sum(a == 2))
unique, counts = np.unique(a, return_counts=True)
print(unique, counts)



