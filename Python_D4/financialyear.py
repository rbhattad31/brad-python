import pandas as pd
months =  {'month':['Jan 2022', 'Feb 2022', 'Mar 2022', 'April 2022', 'May 2022', 'June 2022', 'July 2022', 'Aug 2022', 'Sep 2022', 'Oct 2022', 'Nov 2022', 'Dec 2022']}
df = pd.DataFrame(months)
df['month'] = pd.to_datetime(df['month'])
print(df)

#
# df['Fiscal Year'] = df['As Quarter'].dt.qyear
# print(df)