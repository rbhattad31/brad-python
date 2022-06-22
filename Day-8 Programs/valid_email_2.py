import re

email = input("Enter the mail-id: ")
if re.match(r'[^@]+@[^@]+\.[^@]+', email):
    print("email is valid")
else:
    print("email is not valid")