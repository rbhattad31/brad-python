import random
# return different value every time
print(random.random())

# return same value every time
random.seed(10)
print(random.random())

# return random in between  value
print (random.randrange(10,100))

# return specified no. of bits
print(random.getrandbits(16))

# returns multiple random elements from the list
mylist = ["apple", "banana", "mango"]
print(random.choices(mylist, k =5))

# A random integer in range [start, end] including the end points.
print(random.randint(-10, -1))

# return shuffle the list
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist)