import pandas as pd


df = pd.DataFrame(
	[[13, 'Amal', 72, 90],
	[32, 'Raj', 78, 69],
	[15, 'Ram', 74, 56],
	[52, 'Yuval', 54, 76]],
	columns=['roll-no', 'name', 'physics', 'botany'])

print('DataFrame with default index\n', df)


df = df.set_index('roll-no')

print('\nDataFrame with column as index\n',df)