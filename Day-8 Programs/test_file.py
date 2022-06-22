import re


def oct_to_dec(octal):

    decimal_value = int(octal, 8)
    print(decimal_value)
    return decimal_value


def check_octal(row_no, format_str, no):
    if re.match(r"[0-7]", str(format_str)):
        current_val = oct_to_dec(str(format_str))
        if no == current_val:
            print('row {} is octal'.format(row_no))
        else:
            print("failed-1")
    else:
        print("failed")


print(check_octal(5, 62, 50))
