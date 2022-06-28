import json
import csv


with open('file.json') as json_file:
    data = json.load(json_file)

employee_data = data['employees']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)


count = 0

for emp in employee_data:
    if count == 0:
        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

data_file.close()

import csv
import json


def csv_to_json(csvFile, jsonFile):
    jsonArray = []

    # read csv file
    with open(csvFile, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFile, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'File.csv'
jsonFilePath = r'Data_File.json'
csv_to_json(csvFilePath, jsonFilePath)
