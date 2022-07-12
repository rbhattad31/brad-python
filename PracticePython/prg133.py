import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'Gvinay@1',
    port='3306',
    database='vinaydb'
)
db= mydb.cursor()
db.execute("show tables")
lst= db.fetchall()
print(lst)
table = input("enter your table name:")
if (table,) in lst:
    print('{} table  exists'.format(table))
else:
    print('{} not exists'.format(table))
mydb.close()