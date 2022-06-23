import pandas as pd

# Read Excel file
df = pd.read_excel('sample_excel.xlsx')

# Display last 10 rows
print(df.tail(n=10))

# Set background color
# print(df.style.set_properties(**{'border': '1.3px solid green', 'color': 'magenta'}))

# Highlight max
# df.style.highlight_max()

# Highlight min
# df.style.highlight_min()

# Null color green
# df.style.highlight_null(null_color="green")

# Add Captions
# df.style.set_caption("This is program").set_precision(2).background_gradient()

# we can create own function for coloring
# def color_negative_red(val):
# color = 'red' if val < 0 else 'black'
# return 'color: %s' % color
# df.style.apply(color_negative_red)

# Export to excel
# df.style.set_precision(2).background_gradient().hide_index().to_excel('styled.xlsx', engine='openpyxl')
