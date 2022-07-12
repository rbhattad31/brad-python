import mysql.connector

# Connecting from the server
conn = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    port='3307'
)
db = conn.cursor()
db.execute("show databases")
lst = db.fetchall()
data_base = input("enter database name")
if(data_base,) in lst:
    print("database already exists")
else:
    db.execute("create database {}".format(data_base))
    print("database created")
