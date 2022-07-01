import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()
Tb = 'employee'

# Add Row
query = "INSERT INTO {} (Emp_id, Emp_Name) VALUES (%s, %s)".format(Tb)
val = [('2', 'Peter'), ('3', 'Amy')]
cursor.execute(query, val)

# Add Column
query = "ALTER TABLE students ADD stream VARCHAR(100)"
cursor.execute(query)

# closing DB
cursor.commit()
cursor.close()