import csv

# csv read file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line1 in csv_reader:
        print(line1)

import csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

# csv write file
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')

        for line in csv_reader:
            csv_writer.writerow(line)

import csv
# parse file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line1 in csv_reader:
       print(line1)