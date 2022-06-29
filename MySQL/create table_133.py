import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()

# Get tables
cursor.execute("SHOW TABLES")
Tables = []
for x in cursor:
    for i in x:
        Tables.append(i)
print(Tables)
Tb = 'employee'

# Read table
if Tb in Tables:
    cursor.execute("Select * from {}".format(Tb))
    result = cursor.fetchall()
    for x in result:
        print(x)
else:
    # Create a new table
    cursor.execute("CREATE TABLE {} (Emp_id VARCHAR(255) PRIMARY KEY, Emp_Name VARCHAR(255))".format(Tb))
    cursor.execute("Select * from {}".format(Tb))
    # Adding new data
    query = "INSERT INTO {} (Emp_id, Emp_Name) VALUES (%s, %s)".format(Tb)
    val = [('2', 'Peter'), ('3', 'Amy')]
    cursor.execute(query, val)
    result = cursor.fetchall()
    for x in result:
        print(x)