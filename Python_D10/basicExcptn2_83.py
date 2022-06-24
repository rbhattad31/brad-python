import os
# ImportError
try:
    from time import datetime
except ImportError as e:
    print(e)
# # IndexError
list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[8])

for a in range(0, 6):
    print(list1[a])

#  Key Error
ages = {'Sai': 25, 'Akhil': 25, 'Stark': 28}
person = input('Get age for: ')
age = ages.get(person)

if age:
    print(f'{person} is {age} years old')
else:
    print(f"No records found  with the name {person} ")
# Keyboard interrupt
os.system("clear")
try:
    name = input("Type your name")
    print('your name is ', name)
except KeyboardInterrupt:
    print('ERROR')
