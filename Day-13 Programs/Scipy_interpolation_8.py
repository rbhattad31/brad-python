from scipy import interpolate
import numpy as np

# 1D Interpolation
arr_1 = np.arange(10)
arr_2 = 2 * arr_1 + 3
interp_func = interpolate.interp1d(arr_1, arr_2)
new_arr = interp_func(np.arange(2, 9, 1))
print("1D-interpolation\n:")
print(new_arr)
print()

# Spline interpolation
arr_1 = np.arange(10)
arr_2 = 2 * arr_1 + 3
interp_func = interpolate.UnivariateSpline(arr_1, arr_2)
new_arr = interp_func(np.arange(2, 9, 1))
print("Spline-interpolation\n:")
print(new_arr)
print()

# Radial basis interpolation
arr_1 = np.arange(10)
arr_2 = 2 * arr_1 + 3
interp_func = interpolate.Rbf(arr_1, arr_2)
new_arr = interp_func(np.arange(2, 9, 1))
print("Radial basis-interpolation\n:")
print(new_arr)
print()

