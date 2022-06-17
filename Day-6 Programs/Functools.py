from functools import *


def power(a, b):
    return a**b


Func1 = partial(power, b=2)
Func2 = partial(power, b=4)
Func3 = partial(power, 5)

# partial.func[return function name along with hex value]
print('Function used in partial function Func1 :', Func1.func)
# partial.keywords[return default keyword]
print('Default keywords for Func2 :', Func2.keywords)
# partial.keywords[return arguments]
print('Default arguments for Func3 :', Func3.args)

# use reduce function
list1 = [10, 12, 15, 13, 20]
sum_n = reduce(lambda a, b: a + b, list1)
print(sum_n)

# use lru cache


@ lru_cache(maxsize=None)
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


for n in range(7):
    print(factorial(n), end=' ')
print(factorial.cache_info())

# single dispatch[we can use this overload or override depends upon its type]


@singledispatch
def display(s):
    print(s)


@display.register(int)
def _(s):
    print(s * 2)


display('hello')
display(5)


