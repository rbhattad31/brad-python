x = abs(0-1j)
print(x)

mylist = [0, 1, 1]
x = all(mylist)
print(x)

mylist = [False, True, False]
x = any(mylist)
print(x)

x = ascii("My name is Ståle")
print(x)

x = bin(36)
print(x)

x = bool(1)
print(x)

x = bytearray(2)
print(x)

x = bytes(4)
print(x)

x = chr(97)
print(x)

x = complex(3, 5)
print(x)


class Student:
    name = "Jim"
    age = 30
    country = "Japan"


print(dir(Student))


x = divmod(5, 2)
print(x)


x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))


x = 'print(55)'
eval(x)


def x():
    print(callable(x))


class Person:
    name = "John"
    age = 36
    country = "Norway"


delattr(Person, 'age')
print(Person().name)
print(Person().age)
