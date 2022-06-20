import csv
import json
import csv

with open('employee_names.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    data = {"details": []}
    for row in reader:
        data['details'].append({"EMPLOYEE_ID": row[0], "FIRST_NAME": row[1], "LAST_NAME": row[2], "PHONE_NUMBER": row[3]})

with open('new_emp.json', 'w') as nf:
    json.dump(data, nf, indent=2)

#     Json to csv

with open("new_emp.json") as r:
    reader1 = json.load(r)

with open("afterConvert.csv", "w") as w:
    csv_file = csv.writer(w)
    csv_file.writerow([])
    for item in reader1["details"]:
        csv_file.writerow([])


