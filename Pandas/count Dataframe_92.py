import pandas as pd
df = pd.read_csv('MovieData.csv')
result = df.shape
print("Number of rows and columns of the DataFrame:")
print(result)