import pandas as pd
import numpy as np
exam_data = {'name':['anil','kumar','vinay','vijay','bablu','ratna'],
             'score':[21,34,32,54,np.nan,32],
             'attempts':[1,2,1,2,1,2],
             'qualify':['yes','no','yes','yes','no','yes'],}
labels = ['a','b','c','d','e','f']
df = pd.DataFrame(exam_data ,index=labels)
total_rows= len(df.axes[0])
total_cols=len(df.axes[1])
print("number of rows:"+str(total_rows))
print("number of colums:"+str(total_cols))
