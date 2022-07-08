from scipy.special import cbrt
from scipy.special import exp10

# fetch the element-wise cube root of x
result = cbrt([10, 9, 0.1254, 234])
print(result)

# compute 10**x element wise
result1 = exp10([2, 9])
print(result1)
