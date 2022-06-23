import pandas as pd

data_1 = pd.DataFrame({'id': ['1', '2', '3'], 'name': ['Demo_1', 'Demo_2', 'Demo_3'], 'amount': [210, 100, 920]})

data_2 = pd.DataFrame({'id': ['4', '5', '6'], 'name': ['Demo_4', 'Demo_5', 'Demo_6'], 'amount': [201, 200, 198]})

print("Dataframe - 1:")
print(data_1)
print()
print("Dataframe - 2:")
print(data_2)
print()
print("After Merging:")
result_data = pd.concat([data_1, data_2])
print(result_data)
