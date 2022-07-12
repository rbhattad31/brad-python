import mysql.connector

conn = mysql.connector.connect(
    user='root',
    host='localhost',
    port='3307'
)
mycursor = conn.cursor()
mycursor.execute("Grant all on *.* to python@localhost")
mycursor.execute("Show grants for python@localhost")
result = mycursor.fetchall()
print(result)
mycursor.execute("Flush Privileges")
conn.close()
