import mysql.connector

conn = mysql.connector.connect(
        user='root',
        host='127.0.0.1',
        database='python',
        port='3307'
    )
mycursor = conn.cursor()
mycursor.execute("create table employee_details_copy select * from employee_details")
mycursor.execute("Show tables")
query1 = mycursor.fetchall()
for i in query1:
    print(i)

mycursor.execute("Select * from employee_details_copy")

query2 = mycursor.fetchall()
for i in query2:
    print(i)

# get the table size

query = "SELECT  table_name AS `Table`, \
        round(((data_length + index_length) \
        / 1024 / 1024), 2) `Size in MB` \
        FROM information_schema.TABLES \
        WHERE table_schema = 'python' AND \
        table_name = 'employee_details';"

mycursor.execute(query)

# Display size of each table
result = mycursor.fetchall()

for item in result:
    print(item[0], "Size in MB: ", item[-1])

# renaming table

query = "ALTER TABLE employee_details RENAME to employees"
# Execute the query
mycursor.execute(query)

# Print names of all tables in the database
mycursor.execute("SHOW TABLES")
result2 = mycursor.fetchall()
for row in result2:
    print(row)

# delete an element
query = " DELETE FROM employees  WHERE emp_name = 'Tywin';"
mycursor.execute(query)
conn.commit()

print(mycursor.rowcount, "record(s) deleted")
conn.close()

# Close database connection
conn.close()
