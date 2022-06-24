import re

def isValidDebitCardNo(string):

    regex = "^4[0-9]{12}(?:[0-9]{3})?$"

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if string == '':
        return False

    # Pattern class contains matcher()
    # method to find matching between
    # given string and regular expression.
    m = re.match(p, string)

    # Return True if the string
    # matched the ReGex else False
    if m is None:
        return False
    else:
        return True


if __name__ == "__main__":
    # Test Case 1
    str1 = "4155279860457"
    print(isValidDebitCardNo(str1))

    # Test Case 2
    str2 = "4155279860457201"
    print(isValidDebitCardNo(str2))

    # Test Case 3
    str3 = "4155279"
    print(isValidDebitCardNo(str3))

    # Test Case 4
    str4 = "6155279860457"
    print(isValidDebitCardNo(str4))

    # Test Case 5
    str5 = "415a27##60457"
    print(isValidDebitCardNo(str5))
