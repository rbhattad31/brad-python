# memory error
import random
import os

import self as self

f = "AskHRMVP Total_Utters.csv"
# r = open(f)
# result = r.read()
# print(result)
num_lines = sum(1 for i in open(f))
print(num_lines)
size = num_lines // 2
print(size)
ids = random.sample(range(1, num_lines), size)
print(ids)

# NameError
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
# add = x+y+z
# print(add)
fruit = "Apple"


def Fruit():
    try:
        print(mango)
    except NameError:
        print("Variable is not defined or incorrect variable name")


Fruit()


# NotImplementedError
#
# class Animal:
#     def def_init_(self, name):
#         self.name = name
#
#     def sound(self):
#         raise NotImplementedError("You must take sound from every animal")
#
#
# class Dog(Animal):
#     def def_init_(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#
# class Cat(Animal):
#     def def_init_(self, name, color):
#         super().__init__(name)
#         self.color = color
#
#
# o1 = Dog()
# print(o1.sound())

# OS Error

r, w = os.pipe()
try:
    print(os.ttyname(1))
except OSError as e1:
    print(e1)


