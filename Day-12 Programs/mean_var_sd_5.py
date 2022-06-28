import numpy as np

# Original array
arr = np.arange(36)
x = np.reshape(arr, [4, 9])
print(x)

# mean
mean_1 = np.mean(x)
avg_1 = np.average(x)
print("\nMean, Average: ", mean_1, ',', avg_1)

std = np.std(x)
std_for = np.sqrt(np.mean((x - np.mean(x)) ** 2))
print("\nstd[inbuilt,Formula]: ", std, ',', std_for)

var = np.var(x)
var_for = np.mean((x - np.mean(x)) ** 2)
print("\nvariance[inbuilt,Formula]: ", var, ',', var_for)

