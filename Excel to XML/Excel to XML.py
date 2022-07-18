# Create an Excel spreadsheet that contains a dataset for example - Employees data such as Name, ID, Role, Department
# and City, covert this data to XML format using Python.

import pandas as pd
from lxml import etree as et

raw_data = pd.read_excel(r'Book1.xlsx')

print(raw_data)

root = et.Element('root')

for row in raw_data.iterrows():  # ==> This is a loop that takes runs through each record and populates for each tag.
    root_tags = et.SubElement(root, 'ExportData')  # === > Root name
# These are the tag names for each row (SECTION 1)
    Column_heading_1 = et.SubElement(root_tags, 'GenderSize')
    Column_heading_2 = et.SubElement(root_tags, 'Gender')
    Column_heading_3 = et.SubElement(root_tags, 'ID')
    Column_heading_4 = et.SubElement(root_tags, 'Condition')
    Column_heading_5 = et.SubElement(root_tags, 'State')

# These are the values that will be populated for each row above


# The values inside the [] are the raw file column headings.(SECTION 2)
    Column_heading_1.text = str(row[1]['GenderSize'])
    Column_heading_2.text = str(row[1]['Gender'])
    Column_heading_3.text = str(row[1]['ID'])
    Column_heading_4.text = str(row[1]['Condition'])
    Column_heading_5.text = str(row[1]['State'])

# This Section outputs the data to a xml file
# Unless you tell it otherwise it saves it to the same folder as the script.
tree = et.ElementTree(root)  # ==> The variable tree is to hold all the values of "root"
et.indent(tree, space="\t", level=0)  # ===> This just formats in a way that the XML is readable
tree.write('output.xml', encoding="utf-8")   # ==> The data is saved to an XML file
