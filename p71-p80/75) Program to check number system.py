# Let us assume we have an Excel file that is error-prone contains a first 20 numbers equivalent numbers in various
# number system such as binary, octal, hexadecimal format. create it first manually and read that Excel file using
# openpyxl and check whether all the numbers are having valid digits for each system. ex- binary should have 0's and 1's
# only, etc.And check the equivalent value is correct or not


import re
import openpyxl

# load excel work book
wb_obj = openpyxl.load_workbook('Numbersystem check.xlsx')

# load active sheet
sheet_obj = wb_obj.active

print(sheet_obj)

for row in sheet_obj.iter_rows(0, max_row=20, max_col=3):

    # check each cell value using regex for valid number from the number system
    for cell in row:
        k = cell.value
        # using regex with or operator to check the value for number system
        match = re.match("^[0-1]*$|^0[0-7]*$|^[0-9A-F]+$", k)
        is_match = bool(match)
        print(is_match, end=" ")
    print()
