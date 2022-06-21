#randam password generater

import string
import random

len = int(input("Enter length of the password "))
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbols=string.punctuation

str=lower+upper+digit+symbols
print(str)

