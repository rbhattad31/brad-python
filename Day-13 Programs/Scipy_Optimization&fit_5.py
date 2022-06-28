import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import optimize


def function(arr, a_1, b_1):
    return a_1 * arr + b_1


def test(x_1, a_1, b_1):
    return a_1 * np.sin(b_1 * x_1)


# Method -1[Fit straight line to random data]
x = np.linspace(start=-30, stop=10, num=40)
y = function(x, 4, 2)
np.random.seed(6)
noise = 20 * np.random.normal(size=y.size)
y = y + noise
popt, cov = scipy.optimize.curve_fit(function, x, y)
a, b = popt
x_new_value = np.arange(min(x), 25, 4)
y_new_value = function(x_new_value, a, b)
plt.scatter(x, y, color="green")
plt.plot(x_new_value, y_new_value, color="red")
plt.xlabel('X')
plt.ylabel('Y')
print("Estimated value of a : " + str(a))
print("Estimated value of b : " + str(b))
plt.show()

# Method-2[Curve Fitting]
x = np.linspace(0, 10, num=40)
y = 10.45 * np.sin(5.334 * x) + np.random.normal(size=40)
param, param_cov = optimize.curve_fit(test, x, y)
print("Sine coefficients:")
print(param)
print("Covariance coefficients:")
print(param_cov)
ans = (param[0] * (np.sin(param[1] * x)))
plt.plot(x, y, 'o', color='red', label="data")
plt.plot(x, ans, '--', color='blue', label="optimized data")
plt.legend()
plt.show()
