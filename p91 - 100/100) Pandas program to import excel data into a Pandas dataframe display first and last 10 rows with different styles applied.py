import pandas as pd
df = pd.read_excel('Salesdocument.xlsx')
last_ten = df.tail(n=10)
print(last_ten)
