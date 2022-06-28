import json
import csv

print("Program to demonstrate conversion of json to csv")

print("\n")

with open('sample68a.json') as json_file:
    info = json.load(json_file)

print("JSON file sample68a.json is opened for reading")

print("\n")

emp_info = info['emp_details']
csv_file = open('test.csv', 'w')

print("CSV file is opened for writing JSON data")

print("\n")

csv_writer = csv.writer(csv_file)

count = 0

print("Writing headers to file")

print("\n")

for emp in emp_info:

    if count == 0:

        header_csv = emp.keys()

        csv_writer.writerow(header_csv)

        count += 1

csv_writer.writerow(emp.values())

print("JSON file is converted to CSV file")

csv_file.close()
