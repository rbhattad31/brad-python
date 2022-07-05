# valid mobile number using regex

import re

def isvalid(num):
    pattern = re.compile('(0|91)?[-\s]?[6-9]\d{9}')
    return pattern.match(num)
num = input('enter the number:')
if isvalid(num):
    print('valid:')
else:
    print('invalid num')
