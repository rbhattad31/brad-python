import pandas as pd

emp_data1 = pd.DataFrame({
    'emp_id': ['E1', 'E2', 'E3', 'E4', 'E5'],
    'emp_name': ['Danielle Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'salary': [20000, 31000, 19000, 28000, 19000]})

emp_data2 = pd.DataFrame({
    'emp_id': ['E6', 'E7', 'E8', 'E9', 'E10'],
    'emp_name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
    'salary': [35000, 27000, 50000, 40000, 38000]})

print("Original DataFrames:")
print(emp_data1)
print("***************************************")
print(emp_data2)
print("***************************************")
result_data = pd.concat([emp_data1, emp_data2], axis=1)
print(result_data)
