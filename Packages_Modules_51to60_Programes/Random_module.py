import random

# randrange
print(random.randrange(5))
print(random.randrange(50, 100))
# random
print(random.random())
# randint
print(random.randint(1, 6))
# uniform
print(random.uniform(31, 50))
# choice
list = ["Python", "Java", "C#", ".NEt", "C"]
print(random.choice(list))
string = 'pramod'
print(random.choice(string))

tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(random.choice(tuple))
# shuffle
list1 = [1, 2, 3, 4, 5, 6]
random.shuffle(list1)
print(list1)
