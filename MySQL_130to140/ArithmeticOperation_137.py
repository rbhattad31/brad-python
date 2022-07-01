import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()

# Query
Query = "SELECT sale_price,tax, concat(sale_price+tax) AS amount FROM Sales"
cursor.execute(Query)
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close Connection
connection.close()