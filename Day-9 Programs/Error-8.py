import pandas as pd
import math

# unicode encode error
try:
    u"\u0411".encode("iso-8859-15")
except Exception as e:
    print(e)

# unicode decode error
try:
    dataframe = pd.read_csv('sample.csv')
    print(dataframe)
except Exception as e:
    print(e)

# value error
try:
    print(math.sqrt(-1))
except ValueError as e:
    print('value error', e)

# Zero division error


def formula_1(a, b):
    try:
        c = ((a+b) // (a-b))
        print(c)
    except ZeroDivisionError:
        print("a/b result in 0")


formula_1(2.0, 2.0)


