import pandas as pd
import numpy as np

dict1 = {'First Score': [100, 90, np.NAN, 95],
         'Second Score': [30, 45, 56, np.NAN],
         'Third Score': [np.NAN, 40, 80, 98]}


df = pd.DataFrame(dict1)


df.replace(np.NAN, 0, inplace=True)


df.fillna(value=0, inplace=True)


df.interpolate(inplace=True)

print(df)
