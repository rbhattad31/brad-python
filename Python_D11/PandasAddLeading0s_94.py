import pandas as pd
nums = {'amount': [1, 25, 10, 250, 3000, 40000, 500000]}

df = pd.DataFrame(nums)
print(df)
print("\nAdd leading zeros:")
df['amount'] = df['amount'].apply(lambda x: '{0:0>8}'.format(x))
print(df)
