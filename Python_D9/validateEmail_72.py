import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
user_id = input("Enter your email id:")
if re.search(pattern, user_id):
    print('Login success')
else:
    print("please enter valid email id")
