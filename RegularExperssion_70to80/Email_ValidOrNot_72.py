import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(Email):
    
    if re.fullmatch(regex, Email):
        print("Valid Email")

    else:
        print("Invalid Email")


if __name__ == '__main__':
    email = "pramod@6766.com"
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "pramod@6766.com"
    check(email)
