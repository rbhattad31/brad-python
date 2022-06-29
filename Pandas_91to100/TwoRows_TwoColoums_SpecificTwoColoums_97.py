import pandas as pd

# reading file with std encoding for windows
df = pd.read_csv('sample.csv', encoding='iso-8859-1')

print(df.head())

# Two Row
print("\nSelect first 2 rows:")
print(df.iloc[:2].head())

# Two Column
print("\nSelect first 2 columns:")
print(df.iloc[:, :2].head())

# Specific Column
print("\nSelect 2 specific columns:")

print(df[['D_1', 'D_2']])
