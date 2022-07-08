import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Phoenix@09871234",
  database="world",
)

cursor = mydb.cursor()

#   copy table city into city2
query = "CREATE TABLE city2 SELECT * FROM city"
cursor.execute(query)

#   select rows from the new table
query1 = "SELECT * FROM city"
cursor.execute(query1)

#   print the contents of the copied table
for row in cursor:
    print(row)


mydb.close()
