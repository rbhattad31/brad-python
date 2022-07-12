# import required modules
import mysql.connector

# establish connection to SQL database
connection = mysql.connector.connect(

    # specify hostname
    host="localhost",

    # specify user of mysql database
    user="root",

    # specify password for above user
    password="Gvinay@1",

    # default port number for mysql is 3306
    port=3306,

    # specify database name on which you want to work
    db="vinaydb"
)

# make a cursor
mycursor = connection.cursor()

mycursor.execute("create table select * from table1")

# list all the tables
mycursor.execute("Show tables")

# fetchall() will store all the names
# of tables into query1
query1 = mycursor.fetchall()

# print name of tables
for i in query1:
    print(i)

# read all records from copy table
mycursor.execute("Select * from table1")

# fetchall() will store all the records
# of copy table into query2
query2 = mycursor.fetchall()

# print all records
for i in query2:
    print(i)
