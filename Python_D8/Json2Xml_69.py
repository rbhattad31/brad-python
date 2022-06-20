import json

with open("new_emp.json") as f:
    data = json.load(f)
    print(data)

import xml.etree.cElementTree as ET

root = ET.Element("root")
# result = ET.SubElement(root, "details")
#
# for i in data['details']:
ET.SubElement(root, 'EMPLOYEE_ID').text = data['EMPLOYEE_ID']
ET.SubElement(root, "FIRST_NAME").text = data["FIRST_NAME"]
ET.SubElement(root, "LAST_NAME").text = data["LAST_NAME"]
ET.SubElement(root, "PHONE_NUMBER").text = data["PHONE_NUMBER"]
tree = ET.ElementTree(root)
tree.write("employee.xml")
