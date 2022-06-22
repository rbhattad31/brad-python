
import json
import xmltodict
with open("Data.xml", 'r') as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)
with open("sample3.json", "w") as json_file:
    json_file.write(json_data)
    json_file.close()
