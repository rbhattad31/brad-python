# reduce
from functools import reduce
a = [1,2,3,4]
result = reduce(lambda x,y:x*y, a)
print(result)

# total_ordering

from functools import total_ordering
@total_ordering
class num:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        # Changing the functionality
        # of equality operator
        return self.value != other.value

print(num(2) < num(3))
print(num(2) > num(3))
print(num(3) == num(3))
print(num(3) == num(5))

# lru_cache

from functools import lru_cache
@lru_cache
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')
print(count_vowels("Welcome to New World"))

# partial
from functools import partial
def add(c,b):
    print(c+b)
    return c+b
add_one = partial(add, c=1)
add_one(b = 4)

# wrapper
def decorator(cls):
    class Wrapper:

        def __init__(self, z):
            self.wrap = cls(z)

        def get_name(self):
            # fetches the name attribute
            return self.wrap.name

    return Wrapper


@decorator
class C:
    def __init__(self, y1):
        self.name = y1

# C = decorator(C)
x1 = C("Hello World")
print(x1.get_name())

