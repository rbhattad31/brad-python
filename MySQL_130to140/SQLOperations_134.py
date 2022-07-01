import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()

# Insert Query
sql = "INSERT INTO Demo_1 (Emp_id, Emp_Name) VALUES (%s, %s)"
val = ("4", "Blue")
cursor.execute(sql, val)

# Select Query
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

# Update Query
Query = "UPDATE Demo_1 SET Emp_id = '123' WHERE Emp_Name = 'Blue'"
cursor.execute(Query)

# Where Query
Query = "SELECT * FROM Demo_1 WHERE Emp_Name = 'Blue'"
cursor.execute(Query)

# Order By
Query = "SELECT * FROM Demo_1 ORDER BY Emp_id"
cursor.execute(Query)

# Delete Query
Query = "DELETE FROM Demo_1 WHERE Emp_Name = 'Blue'"
cursor.execute(Query)

# Drop Table
Query = "DROP TABLE Demo_1"
cursor.execute(Query)

# Limit Query
cursor.execute("SELECT * FROM Demo_1 LIMIT 5")
result = cursor.fetchall()
