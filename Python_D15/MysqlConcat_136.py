import mysql.connector

conn = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    database='python',
    port='3307'
)
mycursor = conn.cursor()

mycursor.execute("SELECT Concat(emp_name, emp_id) AS fulldetail FROM employees;")

result = mycursor.fetchall()

for x in result:
    print(x)
