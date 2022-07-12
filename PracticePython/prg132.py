#check if a databse exist , if not create a database and connect to it
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'Gvinay@1',
    port='3306',
    database='vinaydb'
)

db=mydb.cursor()
db.execute('show databases')
lst=db.fetchall()
data_name=input("enter database name")
if (data_name,) in lst:
    print("exists")
else:
    db.execute("create database{}".format(data_name))
    print("data created")
