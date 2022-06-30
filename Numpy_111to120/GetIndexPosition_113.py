import numpy as np

# Creating 1-D Numpy array
a1 = np.array([11, 10, 22, 30, 33])
print("Array 1 :")
print(a1)

a2 = np.array([1, 15, 60])
print("Array 2 :")
print(a2)

print("\nTake 1 and 15 from Array 2 and put them in\
1st and 5th position of Array 1")

a1.put([0, 4], a2)

print("Resultant Array :")
print(a1)