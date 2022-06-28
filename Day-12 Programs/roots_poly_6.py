import numpy as np

# Root of  [x4 − 11x3 + 9x2 + 11x – 10] polynomial
co_efficients = [1, 2, 1]
print("Method-1")
print(np.roots(co_efficients))

# Method-2
p = np.poly1d(co_efficients)
root_of_poly = p.r
print("Method-2")
print(root_of_poly)
