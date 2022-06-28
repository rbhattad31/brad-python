import pandas as pd
import numpy as np
df = pd.read_excel('Employee_data_xls.xls')
op = df.tail(n=10)
print(op)
