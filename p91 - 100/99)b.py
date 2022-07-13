import pandas as pd
df = pd.read_excel('PivotExample.xlsx')
print(df)
pd.pivot_table(df, index=["Product", "Amount"])
