import mysql.connector
conn = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    database='python',
    port='3307'
)
db = conn.cursor()
# db.execute("create table employee_details(emp_name varchar(20), emp_id int(10), designation varchar(20))")
db.execute("show tables")
lst = db.fetchall()
print(lst)
table = input("enter your table name")
if(table, ) in lst:
    print("{} table already exists".format(table))
else:
    print("{} table not exists".format(table))
    db.execute("create table employee_details(emp_name varchar(20), emp_id int(10), designation varchar(20))")
    print("{} table created".format(table))

