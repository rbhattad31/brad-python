import mysql.connector

conn = mysql.connector.connect(
        user='root',
        host='127.0.0.1',
        database='python',
        port='3307'
    )
mycursor = conn.cursor()
# Adding row at the end of table
query = "ALTER TABLE employee_details \
            ADD address VARCHAR(100) "

mycursor.execute(query)


mycursor.execute("desc employee_details")
result = mycursor.fetchall()
for row in result:
    print(row)

# Adding row

sql = """INSERT INTO employee_details (emp_name, emp_id, designation, address) 
                           VALUES 
                           ('Cersi', '1171', 'PHP Developer', 'Winterfell') """


mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount, "Record inserted successfully into employee_details table")

conn.close()
