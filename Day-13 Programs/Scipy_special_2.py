from scipy.special import *
import numpy as np

# cube root function
cube_result = cbrt([100, 59, 260, 34])
print('Cube-root Result: \n', cube_result)

# Exponential function
expo_result = exp10([5, 8])
print('Expo-root Result: \n', expo_result)

# Log sum exponential function
arr = np.arange(10)
log_sum_result = logsumexp(arr)
print('Log_Sum-root Result: \n', log_sum_result)

# Lambert function
w = lambertw(1)
print('Lambert function: \n', w)
print(w * np.exp(w))

# Combination function
combination_result = comb(10, 3, exact=False, repetition=True)
print('Combination function: \n', combination_result)

# permutation function
permutation_result = perm(10, 3, exact=True)
print('Permutation function: \n', permutation_result)

# Gamma function
Gamma_result = gamma([10, 0.5, 1, 5])
print('Gamma function: \n', Gamma_result)

