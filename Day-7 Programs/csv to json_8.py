import csv
import json


# csv to python
def make_json(csv_file_path, json_file_path):
    json_array = []
    with open(csv_file_path, encoding='utf-8') as csv_f:
        csvreader = csv.DictReader(csv_f)
        for row in csvreader:
            json_array.append(row)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(json_array, indent=4))


csvfile_path = r'sample_csv.csv'
jsonfile_path = r'sample2.json'
make_json(csvfile_path, jsonfile_path)
