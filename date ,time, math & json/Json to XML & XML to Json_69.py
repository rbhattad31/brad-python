import json as j

with open("file.json_69") as json_format_file:
  d = j.load(json_format_file)

import xml.etree.cElementTree as e

r = e.Element("Employee")

e.SubElement(r,"Name").text = d["Name"]

e.SubElement(r,"Designation").text = d["Designation"]

e.SubElement(r,"Salary").text = str(d["Salary"])

e.SubElement(r,"Age").text = str(d["Age"])

project = e.SubElement(r,"Projects")

for z in d["Projects"]:
  e.SubElement(project,"Topic").text = z["Topic"]
  e.SubElement(project,"Category").text = z["Category"]
  e.SubElement(project,"Months").text = str(z["Months"])


a = e.ElementTree(r)

a.write("json_to_xml.xml")


import json
import xmltodict

# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
with open("File.xml_69") as xml_file:
  data_dict = xmltodict.parse(xml_file.read())
  xml_file.close()


  json_data = json.dumps(data_dict)


  with open("data.json_69", "w") as json_file:
    json_file.write(json_data)
    json_file.close()
