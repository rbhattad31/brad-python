import random


random.seed(1)
print(random.random())

print(random.getstate())

print(random.getrandbits(8))

print(random.randrange(3, 9))

print(random.randint(1, 9))

mylist0 = ["apple", "banana", "cherry"]

print(random.choice(mylist0))

mylist1 = ["apple", "banana", "cherry"]

print(random.choices(mylist1, weights=[10, 1, 1], k=14))

mylist2 = ["apple", "banana", "cherry"]
random.shuffle(mylist2)

print(mylist2)

mylist3 = ["apple", "banana", "cherry"]

print(random.sample(mylist3, k=2))

print(random.uniform(20, 60))

print(random.triangular(20, 60, 30))
