import json
import csv

data_dict = {}

# Step 2
# open a csv file handler
with open('test.csv', encoding='utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)

    # convert each row into a dictionary
    # and add the converted data to the data_variable

    for rows in csv_reader:
        # assuming a column named 'No'
        # to be the primary key
        key = rows['emp_name']
        data_dict[key] = rows

# open a json file handler and use json.dumps
# method to dump the data
# Step 3
with open('sample68b.json', 'w', encoding='utf-8') as json_file_handler:
    # Step 4
    json_file_handler.write(json.dumps(data_dict, indent=4))
