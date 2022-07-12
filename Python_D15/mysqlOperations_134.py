import mysql.connector

conn = mysql.connector.connect(
    user='root',
    host='127.0.0.1',
    database='python',
    port='3307'
)
mycursor = conn.cursor()

sql = "INSERT INTO employee_details (emp_name, emp_id, designation) VALUES (%s, %s, %s)"
val = ("John", "1131", "Software Engineer")
mycursor.execute(sql, val)

conn.commit()

print(mycursor.rowcount, "record inserted.")


# Using Select query for fetching table data

mycursor.execute("SELECT * FROM employee_details")

result = mycursor.fetchall()

for x in result:
    print(x)

# using where statement

sql = "SELECT * FROM employee_details WHERE emp_name ='Sai'"

mycursor.execute(sql)

result2 = mycursor.fetchall()

for w in result2:
    print(w)
# Order by statement

sql = "SELECT * FROM employee_details ORDER BY emp_name"

mycursor.execute(sql)

result3 = mycursor.fetchall()

for o in result3:
    print(o)
# Delete statement

sql = "DELETE FROM employee_details WHERE emp_name = 'John'"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "record(s) deleted")

# Update statement

sql = "UPDATE employee_details SET designation = 'software engineer trainee' WHERE designation = 'software engineer tr'"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "record(s) affected")

# Drop table
sql = "DROP TABLE cities"

mycursor.execute(sql)

# Limit
mycursor.execute("SELECT * FROM employee_details LIMIT 2")

result4 = mycursor.fetchall()

for L in result4:
    print(L)

# join
sql = "SELECT \
  employee_details.emp_name AS Employee, \
  cities.name AS Address \
  FROM employee_details \
  INNER JOIN cities ON employee_details.emp_id = 1120"

mycursor.execute(sql)

result4 = mycursor.fetchall()

for j in result4:
    print(j)
