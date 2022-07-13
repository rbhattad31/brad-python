import pandas as pd

w_a_con = pd.read_csv('world_alcohol.csv')
print("World alcohol consumption sample data:")
print(w_a_con.head())
print("\nSelect first 2 rows:")
print(w_a_con.iloc[:2])
print("\nSelect first 2 columns:")
print(w_a_con.iloc[:, :2].head())
print("\nSelect 2 specific columns:")
print(w_a_con[['Display Value', 'Year']])
