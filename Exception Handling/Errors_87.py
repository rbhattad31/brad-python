import sys
import pandas as pd

# systemExit Error
try:
    raise SystemExit
except SystemExit:
    print("Specifying SystemError exception in this block works.")

# Ex-2
try:
    sys.exit(0)
except SystemExit:
    print(" System Exception")


# Type Error

try:
    my_int = 23
    my_str = "23"
    print(my_str + my_int)
except TypeError as e:
    print('Type Error-', e)

# Unbound Local Error

try:

    def calculate_grade(grade):

        if grade > 80:
            letter = "A"
        elif grade > 70:
            letter = "B"
        return letter



    print(calculate_grade(36))
except UnboundLocalError as e:
    print("UnboundLocalError-", e)
# Unicode Error

try:
    dataframe = pd.read_csv('sample.csv')
    print(dataframe)
except UnicodeError as e:
    print("UnicodeError-", e)
