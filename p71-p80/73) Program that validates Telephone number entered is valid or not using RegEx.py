import re


def solve(p):
    pattern = "^\\+?[1-9][0-9]{7,14}$"
    if re.match(pattern, p):
        return True
    return False


s = "+12526337268"
print(solve(s))
