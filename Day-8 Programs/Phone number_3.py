import re


def check_phone_no(no):

    pattern = '(0|91)?[0-9]{9}'
    if re.fullmatch(pattern, no):
        print("Valid Number")
    else:
        print("Invalid Number")


phone_no = input("Enter the phone no: ")
check_phone_no(phone_no)
