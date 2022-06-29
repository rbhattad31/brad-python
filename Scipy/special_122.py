from scipy.special import cbrt

# cube root of 64
print(cbrt(64))

# import combinations
from scipy.special import comb

print(comb(4, 1))

from scipy.special import exp10
# 10 to the power of 2
print(exp10(2))

# import exprel
from scipy.special import exprel

# calculate exprel of 0
print(exprel(0))
from scipy.special import gamma

print(gamma(56))

# import lambert function
from scipy.special import lambertw

# calculate W value
print([lambertw(1), lambertw(0), lambertw(56),
       lambertw(68), lambertw(10)])

from scipy.special import logsumexp

# log sum exp of numbers from
# 1 to 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(logsumexp(a))

# import permutations module
from scipy.special import perm

# permutations of 4
print([perm(4, 1), perm(4, 2), perm(4, 3),
       perm(4, 4), perm(4, 5)])