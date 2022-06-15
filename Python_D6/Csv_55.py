import csv

with open("employees.csv", "r") as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)
    # next(csv_reader)
    # with open("employee_names.csv", "w") as new_file:
    #     csv_writer = csv.writer(new_file, delimiter=',')
    for row in csv_reader:
        # print(row[1],row[2])
        # csv_writer.writerow(row)
        print(row)
