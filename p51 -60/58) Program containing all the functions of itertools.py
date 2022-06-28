import itertools
import itertools as it
from itertools import cycle
from itertools import chain
from itertools import compress
from itertools import dropwhile
from itertools import takewhile
from itertools import groupby


# defining the grouper function
def grouper(inputs, n, fill_value=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=fill_value)


alpha = ['g', 'e', 'e', 'k', 's', 'f', 'o',
         'r', 'g', 'e', 'e', 'k', 's']
print(list(grouper(alpha, 3)))

print(list(it.combinations([1, 2], 2)))

print(list(it.combinations_with_replacement([1, 2], 2)))

print(list(it.permutations(['g', 'e', 'k'])))

list_of_lists = [[1, 2], [3, 4]]
chain_object = it.chain.from_iterable(list_of_lists)

flattened_list = list(chain_object)

print(flattened_list)

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")

list1 = [1, 2, 3, 4]
iterator = cycle(list1)

for i in iterator:
    print(i)

result = list(chain([1, 2, 3],
                    ["one", "two", "three"],
                    "String",
                    ("this", "is", "a", "tuple")))

print(result)

print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

Codes = ['C', 'C++', 'Java', 'Python']
selectors = [False, False, False, True]

Best_Programming = itertools.compress(Codes, selectors)

for each in Best_Programming:
    print(each)

cars = ['Audi', 'Volvo', 'Benz',
        'BMW', 'Nissan', 'Mazda',
        'Ford']

selector = [True, True, False, False,
            False, True, False]

my_cars = compress(cars, selector)

for each in my_cars:
    print(each)

int_list = [0, 1, 2, 3, 4, 5, 6]
result = list(dropwhile(lambda x: x < 3, int_list))

print(result)


def contains_character(str1):
    substring = 'o'
    if substring in str1:
        return True
    else:
        return False


string_list = ['lorem', 'ipsum', 'dolor', 'sit', 'amet']
print(list(takewhile(contains_character, string_list)))

word = "aaabbbccaabbbbb"

for key, group in groupby(word):
    print(key, list(group))
