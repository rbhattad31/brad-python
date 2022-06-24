import pandas as pd
salary = {'amount': [10000, 250000, 30000, 40000, 500000]}
print("Original dataframe:")
df = pd.DataFrame(salary)
print(df)
print("\nAdd leading zeros:")
df['amount'] = df['amount'].apply(lambda x: '{0:0>8}'.format(x))
print(df)