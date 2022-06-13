import sys


def merge(dictionary1, dictionary2):
    res = dictionary1 | dictionary2
    return res


dictionary1 = {'x': 10, 'y': 8}
dictionary2 = {'a': 6, 'b': 4}
dictionary3 = merge(dictionary1, dictionary2)

print(dictionary3)

print("Size of dictionary3 is : " + str(sys.getsizeof(dictionary3)) + " bytes")
