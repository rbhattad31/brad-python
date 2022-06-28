import re


def isValid(P):
    Pattern = re.compile("(0|91)?[7-9][0 -9]{9}")
    return Pattern.match(P)


s = "91994855766"
if isValid(s):
    print("Valid Number")
else:
    print("Invalid Number")
