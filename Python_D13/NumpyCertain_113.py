import numpy as np
inputArray1 = np.array([11, 10, 22, 30, 33])
print("Array 1 :")
print(inputArray1)

inputArray2 = np.array([1, 15, 60])
print("Array 2 :")
print(inputArray2)


inputArray1.put([0, 4], inputArray2)


print("Resultant Array :", inputArray1)
