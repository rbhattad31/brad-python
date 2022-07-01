from scipy.special import cbrt

# cube root of 64
print(cbrt(64))

# cube root of 78
print(cbrt(78))

# cube root of 128
print(cbrt(128))
from scipy.special import cbrt

# cube root of elements in an array
arr = [64, 164, 564, 4, 640]
arr = list(map(cbrt, arr))
print(arr)
# import combinations
from scipy.special import comb

# combinations of input 4
print(comb(4, 1))
# import combinations module
from scipy.special import comb

# combinations of 4
print([comb(4, 1), comb(4, 2), comb(4, 3),
       comb(4, 4), comb(4, 5)])

from scipy.special import exp10

# exponent raise to power 10
# for a range
for i in range(1, 10):
    print(exp10(i))
# import exprel
from scipy.special import exprel

# calculate exprel of 0
print(exprel(0))
from scipy.special import exprel

# list of elements
arr = [0, 1, 2, 3, 4, 5]

print(list(map(exprel, arr)))
# import gamma function
from scipy.special import gamma

print([gamma(56), gamma(156), gamma(0),
       gamma(1), gamma(5)])
# import lambert function
from scipy.special import lambertw

# calculate W value
print([lambertw(1), lambertw(0), lambertw(56),
       lambertw(68), lambertw(10)])
from scipy.special import logsumexp
# logsum exp of numbers from
# 1 to 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(logsumexp(a))
# import permutations module
from scipy.special import perm
# permutations of 4
print([perm(4, 1), perm(4, 2), perm(4, 3),
       perm(4, 4), perm(4, 5)])