import pandas as pd
df = pd.DataFrame({
    'job_code': ['D001', 'T002', 'D003', 'M101', 'T102', 'A041'],
    'Role': ['Developer', 'Tester', 'Developer', 'Marketing', 'Testing', 'Automation'],
    'name': ['Sai', 'Akhil', 'Danni', 'Vijji', 'Stark', 'Cersi'],
    'date_Of_Birth': ['11/06/1997', '7/07/1997', '24/12/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
    'weight': [65, 75, 65, 55, 31, 32],
    'address': ['Chillam cherla', 'Oslo', 'Chillam cherla', 'USA', 'UK', 'England& wales'],
    'emp_id': ['B1145', 'B1122', 'B1243', 'B1922', 'B1525', 'B1526']})
print("Default Index:")
print(df.head(10))
print("\nt_id as new Index:")
df1 = df.set_index('emp_id')
print(df1)
print("\nReset the index:")
df2 = df1.reset_index(inplace=False)
print(df2)
