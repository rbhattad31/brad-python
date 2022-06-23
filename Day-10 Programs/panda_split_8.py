import pandas as pd

# reading file with std encoding for windows
df = pd.read_csv('sample.csv', encoding='iso-8859-1')

print("Original DataFrame:")
print(df)

# Single column
print('\nSplit by single column:')
single = df.groupby(['D_1'])
print("Size")
print(single.size())

# Multiple Column
print('\nSplit by Multiple column:')
multiple = df.groupby(['D_1', 'D_2'])
print("Size")
print(multiple.size())
