import pandas as pd

# reading file with std encoding for windows
df = pd.read_csv('sample.csv', encoding='iso-8859-1')


print("Original DataFrame:")
print(df)
print("\nMissing values of the dataframe:")
df = df.isna()
print(df)  # [There are no missing values in  csv file, so it shows false]

# pivot with multiple index
print()
print("Dataframe with multiple index\n")
print(pd.pivot_table(df, index=["No", "D_1"]))




