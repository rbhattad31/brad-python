import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Phoenix@09871234",
  database="sys",
)

cursor = mydb.cursor()

query = "SELECT Price,tax, concat(Price+tax) AS amount FROM Bills"
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

mydb.close()
