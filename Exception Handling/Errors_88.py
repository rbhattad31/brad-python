import pandas as pd
import math

# unicode encode error
try:
    u"\u0411".encode("iso-8859-15")
except Exception as error:
    print(error)

# unicode decode error
try:
    dataframe = pd.read_csv('File.csv')
    print(dataframe)
except Exception as e:
    print(e)

# value error
try:
    print(math.sqrt(-4))
except ValueError as e:
    print('value error', e)

# Zero division error
# without try &except it is ZeroDivisionError


    try:
        x = 1
        y = 0
        print("Result",x/y)
    except ZeroDivisionError:
        print("x/y result in 0")


