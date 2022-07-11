import re


def solve(p):
    pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pattern, p):
        return True
    return False


s = "axy@comPany.com"
print(solve(s))
