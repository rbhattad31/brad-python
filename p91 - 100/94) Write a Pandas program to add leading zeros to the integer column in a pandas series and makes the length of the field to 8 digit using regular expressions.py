import pandas as pd
import re
ID = {'ID': [2345656, 3456, 541304, 201306, 12313201308]}

print("Original dataframe:")
df = pd.DataFrame(ID)

print(df)

print("\nAdd leading zeros:")
df['ID'] = df['ID'].apply(lambda x: '{0:0>8}'.format(x))  # .str.extract(r'(^w{5})')

print(df)


def limit_number(text):

    _no = re.findall(r"\b\d{8}\b", text)
    return "".join(_no)


print("\nAdd limit to eight digits:")

df['Eight digit'] = df['ID'].apply(lambda x: limit_number(x))

print(df)
