import pandas as pd
from lxml import etree as et
import xml.etree.ElementTree as Xet
import time
from datetime import timedelta

start_time = time.monotonic()
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))
print("--- %s seconds ---" % (time.time() - start_time))

raw_data = pd.read_excel("Copy of F21 Men's US Masterlist.xlsx")
root = et.Element('root')
for row in raw_data.iterrows():
    root_tags = et.SubElement(root, 'Product')
    Column_heading_1 = et.SubElement(root_tags, 'GenderSizeGroup', GenderSizeGroup=str(row[1]['Gender Size Group']))
    # , GenderSizeGroup=str(row[1]['Gender Size Group']))
    Column_heading_2 = et.SubElement(root_tags, 'GenderSizeGroupRoll-Up')
    Column_heading_3 = et.SubElement(root_tags, 'EANUPCNumber')
    Column_heading_4 = et.SubElement(root_tags, 'TurnonUPCs')
    Column_heading_5 = et.SubElement(root_tags, 'Locale')

    # Column_heading_1.text = str(row[1]['Gender Size Group'])
    Column_heading_2.text = str(row[1]['Gender Size Group Roll-Up'])
    Column_heading_3.text = str(row[1]['EAN/UPC Number'])
    Column_heading_4.text = str(row[1]['Turn on UPCs?'])
    Column_heading_5.text = str(row[1]['Locale'])

tree = et.ElementTree(root)
et.indent(tree, space="\t", level=0)
tree.write('F21 Us Masterlist.xml', encoding="UTF-8")
