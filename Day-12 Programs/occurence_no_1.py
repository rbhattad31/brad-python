import numpy as np
arr_1 = np.array([[2, 8, 9, 4], [9, 4, 9, 4], [4, 5, 9, 7], [2, 9, 4, 3]])

# No of occurrences of specified number
print("Specific occurrences")
print(np.count_nonzero(arr_1 == 1))
print(np.count_nonzero(arr_1 == 2))
print(np.count_nonzero(arr_1 == 3))
print(np.count_nonzero(arr_1 == 9))

# Occurrences of sequence
output = repr(arr_1).count("9, 4")
print("Sequence occurrences")
print(output)

