import numpy as np

# Create array of 10 elements
array = np.arange(10)
print("\n", array)

# Calculating average
avg = np.average(array)
print("\nMean: ", avg)

# Calculating standard deviation
std = np.sqrt(np.mean((array - np.mean(array)) ** 2))
print("\nstandard deviation: ", std)

# Calculating variance
var = np.mean((array - np.mean(array)) ** 2)
print("\nvariance: ", var)
