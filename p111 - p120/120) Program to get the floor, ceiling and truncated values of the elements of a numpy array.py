import numpy as np

array = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0])

print("Original array:")
print(array)

print("Floor values of the above array elements:")
print(np.floor(array))

print("Ceil values of the above array elements:")
print(np.ceil(array))

print("Truncated values of the above array elements:")
print(np.trunc(array))
