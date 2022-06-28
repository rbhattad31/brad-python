import pandas as pd

df = pd.read_excel('Employee_data_xls.xls')
print(df)
pd.pivot_table(df, index="last_name", columns='address')
