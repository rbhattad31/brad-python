from scipy.stats import norm
from scipy.stats import uniform
import numpy as np

from scipy import stats


print(norm.cdf(np.array([1, -1., 0, 1, 3, 4, -2, 6])))

# To find the median of a distribution, we can use the Percent Point Function (PPF), which is the inverse of the CDF
print(norm.ppf(0.5))

# To generate the sequence of random values
print(norm.rvs(size=5))

# To generate uniform distribution
print(uniform.cdf([0, 1, 2, 3, 4, 5], loc=1, scale=4))


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("The maximum number of the array is :", x.max())
print("The minimum number of the array is :", x.min())
print("The mean of the array is :", x.mean())
print("The variation of the array is :", x.var())
