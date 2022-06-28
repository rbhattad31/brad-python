import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()

# Grant permission
user = 'root'
cursor.execute("Grant all on *.* to {}@localhost".format(user))
cursor.execute("Show grants for {}@localhost".format(user))
result = cursor.fetchall()
print(result)
cursor.execute("Flush Privileges")

# close connection to MySQL
connection.close()
