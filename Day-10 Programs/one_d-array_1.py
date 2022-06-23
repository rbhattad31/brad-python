import pandas as pd

num_1 = int(input("Enter the 1d-array limit: "))
data_set = []
for i in range(num_1+1):
    data_set.append(i)

print(pd.Series(data_set))
