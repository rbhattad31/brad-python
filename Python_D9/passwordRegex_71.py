import re

pattern = re.compile(r'')
while True:
    password = input("Enter your password")
    if len(password) < 8:
        print("Password must be 8 characters long")
    elif re.search(r'[!@#$%&]', password) is None:
        print("Password must contain one special character")
    elif re.search(r'\d', password) is None:
        print('Password should contain atleast one numeric value')
    elif re.search('[A-Z]', password) is None:
        print("Password must contain one Capital letter")
    elif re.match(r'[a-z A-Z 0-9 !@#$%&]{8}', password):
        pattern = re.compile(r'[a-z A-Z 0-9 !@#$%&]{8}', password)
        result = pattern.match(password)
        print("Login success")
        break
    else:
        print("Password is invalid")
