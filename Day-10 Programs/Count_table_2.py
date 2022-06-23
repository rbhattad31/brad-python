import pandas as pd

# reading file with std encoding for windows
df = pd.read_csv('sample.csv', encoding='iso-8859-1')

# Method - 1
total_rows = len(df.axes[0])
total_cols = len(df.axes[1])
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))
print()

# Method - 2
print("Rows,Columns - ", end='')
print(df.shape)
