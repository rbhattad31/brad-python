
import numpy as np

a1 = np.array([11, 10, 22, 30, 33])
print("Array 1 :")
print(a1)

a2 = np.array([1, 15, 60])
print("Array 2 :")
print(a2)
# Get certain values
print()
print(a1[0])
print(a2[0])

# Add in specific index
a1.put([0, 4], a2[1])
print()
print("Resultant Array :")
print(a1)
