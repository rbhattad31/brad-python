import csv

# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# csv data
rows = [
    {'name': 'Albania', 'area': 28748, 'country_code2': 'AL', 'country_code3': 'ALB'}]

# open Book1 csv
with open('Book1.csv', 'w', encoding='UTF8', newline='') as f:

    # create the csv writer
    writer = csv.writer(f)

    # input data

    writer.writerow(fieldnames)

    writer.writerow(rows)


# create new file countries
with open('countries.csv', 'w', encoding='UTF8', newline='') as f:

    # data writer
    writer = csv.DictWriter(f, fieldnames=fieldnames)
# write header
    writer.writeheader()
# write row data
    writer.writerows(rows)
