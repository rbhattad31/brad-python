import matplotlib.pyplot as plt
import numpy as np

from scipy.stats.mstats import describe
from scipy.stats import randint
from scipy.stats import gmean


# To Compute several descriptive statistics of the passed array
ma = np.ma.array(range(6), mask=[0, 0, 0, 1, 1, 1])
result1 = describe(ma)
print(result1)

# To Calculate geometric mean
print(gmean([1, 4]))

# Using randint module from spicy stats
fig, ax = plt.subplots(1, 1)
low, high = 7, 31
mean, var, skew, kurt = randint.stats(low, high, moments='mvsk')
x = np.arange(randint.ppf(0.01, low, high), randint.ppf(0.99, low, high))
ax.plot(x, randint.pmf(x, low, high), 'bo', ms=8, label='randint pmf')
ax.vlines(x, 0, randint.pmf(x, low, high), colors='b', lw=5, alpha=0.5)
rv = randint(low, high)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()
