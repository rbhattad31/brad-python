import pandas as pd
data_1 = {'Trans_id': [100, 650, 3040, 9040, 54900]}
print("Original dataframe:")
df = pd.DataFrame(data_1)
print(df)
print()
print("Add leading zeros:")
df['Trans_id'] = df['Trans_id'].apply(lambda x: '{0:0>8}'.format(x))
print(df)
