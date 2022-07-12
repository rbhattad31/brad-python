import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'Gvinay@1',
    port='3306',
    database='vinaydb'
)

#mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)