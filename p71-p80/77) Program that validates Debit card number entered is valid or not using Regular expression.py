import re


def check_if_valid_debit_card(string):

    pattern = "^4[0-9]{12}(?:[0-9]{3})?$"

    # Compile the ReGex
    p = re.compile(pattern)

    # If the string is empty
    # return false
    if string == '':
        return False

    # Pattern class contains matcher()
    # method to find matching between
    # given string and regular expression.
    match = re.match(p, string)

    # Return True if the string
    # matched the ReGex else False
    if match is None:
        return False
    else:
        return True


# Driver code
if __name__ == "__main__":
    # Test Case 1
    str1 = "4155279860457"
    print(check_if_valid_debit_card(str1))
