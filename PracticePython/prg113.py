#write a program to get values of an NumPy array at certain index positions
# Importing Numpy module
import numpy as np

# Creating 2-D Numpy array
a1 = np.array([[11, 10, 22, 30],
               [14, 58, 88, 100]])

print("Array 1 :")
print(a1)

a2 = np.array([1, 15, 6, 40])
print("Array 2 :")
print(a2)

print("\nTake 1, 15 and 6 from Array 2 and put them in 1st,\
4th and 7th positions of Array 1")

a1.put([0, 3, 6], a2)

print("Resultant Array :")
print(a1)