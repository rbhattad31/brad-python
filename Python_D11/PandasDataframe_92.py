import pandas as pd

data = {
    "emp_name": ["Vijji", "Sai", "Akhil", "Danni", "john", "ygirette", "tywin", "Catelyn", "Ned", "Namia", "tyrion",
                 "Sansa", "Cersi", "Jaime"],
    "Role": ["Developer", "Tester", "Marketing", "Developer", "Tester", "Marketing", "Developer", "Tester", "Marketing",
             "Developer", "Tester", "Marketing", "Developer", "Tester"],
    "Salary": [30000, 25000, 28000, 30000, 25000, 28000, 30000, 25000, 28000, 30000, 25000, 28000, 30000, 25000]
}

df = pd.DataFrame(data, index=pd.Index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
                  columns=pd.Index(['emp_name', 'Role', 'Salary'], name="S.No"))
print(df)
print(df.shape)
print("No of rows in data frame is :", df.shape[0])
print("No of columns in data frame is :", df.shape[1])
