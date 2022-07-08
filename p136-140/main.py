import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Phoenix@09871234"
)

print(mydb)
