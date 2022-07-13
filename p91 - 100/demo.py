import pandas as pd
import openpyxl

df = pd.read_excel('Salesdocument.xlsx')

table = pd.pivot_table(df, index=["Region", "Manager", "SalesMan"], values="Sale_amt")

print(table.query('Manager == ["Douglas"]'))
