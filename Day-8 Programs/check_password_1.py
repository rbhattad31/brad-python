# Run the program in terminal for getting hidden user input
import re
import getpass
password = getpass.getpass('Enter password:')
if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print("password is valid")
else:
    print("password is not valid")
