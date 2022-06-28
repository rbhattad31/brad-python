import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()

# Query
Query = "SELECT Concat(Column Name 1, Column Name 2) AS full detail FROM Table_Name"
cursor.execute(Query)
result = cursor.fetchall()
for x in result:
    print(x)

# Close Connection
connection.close()
