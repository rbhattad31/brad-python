from scipy.special import cbrt
from scipy.special import comb
from scipy.special import exp10
from scipy.special import exprel
from scipy.special import gamma
from scipy.special import lambertw
from scipy.special import logsumexp

# cube root of the given number
user_input = int(input("Enter any number"))
print(cbrt(user_input))

# comb() :returns the combination of a given value.
# combinations of input 4
print(comb(5, 2))

# exp10():raise to 10 power of the given number.

print(exp10(user_input))

# exprel():returns the error value for a given variable. If x is near zero, then exp(x) is near 1.

# calculate exprel of given input
print(exprel(user_input))

# gamma():  It is the generalized factorial since z*gamma(z) = gamma(z+1) and gamma(n+1) = n!, for a natural number ‘n’.

print(gamma(user_input))

# lambertw() It is also known as Lambert Function. It calculates the value of W(z) is such that z = W(z) * exp(W(z))
# for any complex number z, where W is known as the Lambert Function

# calculate W value
print([lambertw(1), lambertw(0), lambertw(56),
       lambertw(68), lambertw(10)])

# logsumexp():It is known as Log Sum Exponential Function. It will return the log of the sum of the exponential of
# input elements.

# logsum exp of numbers from 1 to 10
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(logsumexp(a))

