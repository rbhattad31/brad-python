import numpy as np

a1 = np.array([11, 10, 22, 30, 33])

a2 = np.array([1, 15, 60])

a1.put([0, 4], a2)

print("Resultant Array :")
print(a1)