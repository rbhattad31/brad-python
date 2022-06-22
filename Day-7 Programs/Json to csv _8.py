import json
import csv

with open('sample2.json') as json_file:
	F_data = json.load(json_file)

data_file = open('sample_csv.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in F_data:
	if count == 0:
		header = F_data.keys()
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(F_data.values())

data_file.close()
