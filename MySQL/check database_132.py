import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', user='root', password='*********')
    cursor = connection.cursor()
    try:
        DB = 'Demo_1'
        cursor.execute("CREATE DATABASE {} ".format(DB))
        print("Database Created Successfully")
    except Exception as e:
        print(e)

except mysql.connector.Error as error:
    print(error)
