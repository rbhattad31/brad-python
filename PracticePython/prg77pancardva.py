import re
pan = input('enter pan number')
result = re.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}")

if result.match(pan):
    print('valid num')
else:
    print('invalid')
