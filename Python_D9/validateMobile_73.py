import re


def isValid(num):
    pattern = re.compile('(0|91)?[-\s]?[6-9]\d{9}')
    return pattern.match(num)


num = input("Enter your mobile number")
if isValid(num):
    print("Login success")
else:
    print("Enter valid number")
