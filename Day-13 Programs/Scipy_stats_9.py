from scipy.stats import *
import numpy as np

# Normal Continuous random variable
arr = np.arange(-5, 1, 0.5)
print(norm.cdf(arr))
print()

# Percent point function
print(norm.ppf(0.05))
print()

# Generate random variates
print(norm.rvs(size=3))
print()

# Uniform Distribution
arr = np.arange(5)
print(uniform.cdf(arr, loc=1, scale=6))
print()

# T-test
# with 1 sample
rvs = norm.rvs(loc=3, scale=10, size=(10, 2))
print(stats.ttest_1samp(rvs, 3.0))

# with 2 sample
rvs1 = norm.rvs(loc=5, scale=10, size=200)
rvs2 = norm.rvs(loc=5, scale=10, size=500)
print(stats.ttest_ind(rvs1, rvs2))
print()

# In_va_gamma method
a = 1
val = invgamma.rvs(a)
print(val)
print()

# Hyp-scent mean method
b = 3
val = hypsecant.mean(b)
print(val)
