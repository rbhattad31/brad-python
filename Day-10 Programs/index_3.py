import pandas as pd

# reading file with std encoding for windows
df = pd.read_csv('sample.csv', encoding='iso-8859-1')

print("Default Index:")
print(df.head(10))
print()
print("No as new Index:")
df1 = df.set_index('No')
print(df1)
print()
print("Reset the index:")
df2 = df1.reset_index(inplace=False)
print(df2)
