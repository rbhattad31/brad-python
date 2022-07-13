import pandas as pd

data = [10, 20, 30, 40, 50, 60]

df = pd.DataFrame(data)

# To print with default index
print(df)

df1 = pd.DataFrame(data, columns=['Numbers'])

print(df1)
