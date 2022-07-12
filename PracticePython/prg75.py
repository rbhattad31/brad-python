import re
import openpyxl

wb_obj = openpyxl.load_workbook('')
sheet_obj= wb_obj.active

print(sheet_obj)

NumRegex = re.compile(r'\b[01]+\b')
for row in sheet_obj.iter_rows(0,max_row=20,max_col=3):
    for cell in row:
        k=cell.value
        match = re.match("^[0-1]*$ | ^[0-7]*$ | ^[0-9A-F]+$",k)
        is_match = bool(match)
        print(is_match, end=' ')
    print()


