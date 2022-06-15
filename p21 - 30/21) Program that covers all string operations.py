string = 'hېLLo WoRLd'

# Original text
print(string)

print(string.upper())

print(string.lower())

print(string.title())

#   Capitalize the first letter
print(string.capitalize())

new_string = string.center(20, '#')
print(new_string)

#   Counts the number of times substring occurs in main string
print(string.count("heLLo"))

print("The encoded string in utf8 format is : ", string.encode(encoding='ascii', errors='namereplace'))

result = string.endswith('d')
print(result)

#   Specifying the space in the string

string1 = 'hېLLo\tWoRLd'
print("Modified string using less spacing: ", end="")
print(string1.expandtabs())
print("\r")

#   To print the lowest index of the substring if it is found in a given string
print(string.find('RL', 2))


print("Hi ! My name is {}, and I am {} years old".format("Anto", 25))

a = {'x': 'Mark', 'y': 'Antony'}
print("{x}'s last name is {y}".format_map(a))

string2 = "A smile goes further than a mile"
print("The first position of mil after 4th index :", string2.index('mil', 4))

#   To check whether all the characters in a given string are alphanumeric or not
print(string.isalnum())

#   To check whether all the characters in a given string are alphabets or not
print(string.isalpha())

print(string.isdecimal())

print(string.isdigit())

print(string.isidentifier())

print(string.islower())

print(string.isnumeric())

print(string.isprintable())

print(string.isspace())

print(string.istitle())

print(string.isupper())

list1 = ['H', 'e', 'l', 'l', 'o']
print("".join(list1))

print(string.rjust(20))

#  String with leading characters removed
print(string.lstrip())
