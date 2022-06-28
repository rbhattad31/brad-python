import functools
import operator
from functools import partial
from functools import lru_cache


def f(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x


g = partial(f, 3, 1, 4)
print(g(5))


@lru_cache(maxsize=100)
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')


print(count_vowels("Welcome to PyCharm Python IDE"))


def compare(a, b):
    print("comparing ", a, " and ", b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


lis = [1, 3, 5, 6, 2]

print(sorted([1, 3, 4, 1], key=functools.cmp_to_key(compare)))

print(min([45, 78, 813], key=functools.cmp_to_key(compare)))

print(max([45, 78, 813], key=functools.cmp_to_key(compare)))

print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

print(functools.reduce(operator.add, lis))

print(functools.reduce(operator.mul, lis))

print(functools.reduce(operator.add, ["apple", "cherry", "watermelon"]))


@functools.total_ordering
class Num:

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value != other.value


print(Num(2) < Num(3))
print(Num(2) > Num(3))
print(Num(3) == Num(3))
print(Num(3) == Num(5))
