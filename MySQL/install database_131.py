import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', user='root', password='*********')
    cursor = connection.cursor()
    print("Database Connected Successfully")

except mysql.connector.Error as error:
    print(error)
