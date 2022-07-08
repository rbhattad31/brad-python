import numpy as np
from scipy import interpolate

array1 = np.arange(0, 10)

array2 = np.arange(10, 20)

result = interpolate.interp1d(array1, array2)

print(result)
