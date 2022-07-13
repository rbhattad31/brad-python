# import numpy library as np
import numpy as np

# import pandas library as pd
import pandas as pd


# List of Tuples
students = [('Ankit', 22, 'Up', 'Geu'),	('Ankita', np.NaN, 'Delhi', np.NaN), ('Rahul', 16, 'Tokyo', 'Abes'),
            ('Simran', 41, 'Delhi', 'Gehu'), ('Shaurya', np.NaN, 'Delhi', 'Geu'), ('Shivangi', 35, 'Mumbai', np.NaN),
            ('Swapnil', 35, np.NaN, 'Geu'), (np.NaN, 35, 'Uk', 'Geu'), ('Jeet', 35, 'Guj', 'Gehu'),
            (np.NaN, np.NaN, np.NaN, np.NaN)]

# Create a DataFrame object from
# list of tuples with columns
# and indices.
details = pd.DataFrame(students, columns=['Name', 'Age', 'Place', 'College'], index=['a', 'b', 'c', 'd', 'e', 'f',
                                                                                     'g', 'i', 'j', 'k'])

# show the boolean dataframe
print(" \nshow the boolean Dataframe : \n\n", details.isnull())

# Count total NaN in a DataFrame
print(" \nCount total NaN in a DataFrame : \n\n", details.isnull().sum().sum())
