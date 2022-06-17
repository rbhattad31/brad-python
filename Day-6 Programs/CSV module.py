import csv

# Read file
with open('Demo.csv', newline='') as f:
    reader = csv.reader(f)
    row_count = 0
    for row in reader:

        if row_count > 10:
            break
        else:
            print(reader.line_num)
            print(row)

        row_count += 1

    f.close()

# use sniffer to read with dialect parameter
print("sniffer-row")
with open('Demo.csv', newline='') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    reader = csv.reader(f, dialect)
    row_count = 0
    for row in reader:
        if row_count > 10:
            break
        else:
            print(row)
        row_count += 1
    f.close()

# Write csv file[Appending use(a) for overwrite use(w)]
data = ['6520903674', 'AFGHAN', 'Khalid', 'A&A', '4']
with open('Demo.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()
