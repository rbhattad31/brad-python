from scipy.optimize import least_squares
import numpy as np


def rosenbrock(x):
    return np.array([10 * (x[1] - x[0] ** 2), (1 - x[0])])


input_ = np.array([2, 2])
result = least_squares(rosenbrock, input_)

print(result)
