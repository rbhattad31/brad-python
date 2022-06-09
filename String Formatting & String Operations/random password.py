import random
import string

Length = int(input("Enter the length of the password: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

All = lower + upper + num + symbols

temp = random.sample(All, Length)
password = "".join(temp)
print(password)