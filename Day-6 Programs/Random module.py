import random

# Generate Random bits
print(random.getrandbits(67))
# Getstate()
print(random.getstate())
# random range element
print(random.randrange(5, 500, 50))
# random element
print(random.randint(1, 20))
# shuffle
x = [1, 2, 45, 25]
random.shuffle(x)
print(x)
# sample
print(random.sample(x, 2))
# random value
print(random.random())
# uniform
print(random.uniform(3, 10))
# triangular
print(random.triangular(10, 5, 100))
# Interval between arrivals averaging 5 seconds
print(random.expovariate(1 / 5))
