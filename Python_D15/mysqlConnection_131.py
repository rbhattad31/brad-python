# Python program to connect
# to mysql database


import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    database='python',
    port='3307'
)
print(conn)

# Disconnecting from the server
conn.close()
