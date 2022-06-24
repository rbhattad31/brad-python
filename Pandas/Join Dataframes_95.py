import pandas as pd

employee_data1 = pd.DataFrame({
        'employee_id': ['001', '002', '003', '004', '005'],
         'employee_name': ['Ram', 'Jake', 'Bryce Jensen', 'Raju', 'Kwame Morin'],
        'salary': [20000, 21000, 19000, 22200, 19900]})

employee_data2 = pd.DataFrame({
        'employee_id': ['140', '150', '106', '187', '108'],
        'employee_name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madhu Preston'],
        'salary': [20100, 20020, 10100, 23200, 20000]})

print("Original DataFrames:")
print(employee_data1)
print("-------------------------------------")
print(employee_data2)
print("\nJoin the said two dataframes along rows:")
result_data = pd.concat([employee_data1, employee_data2])
print(result_data)