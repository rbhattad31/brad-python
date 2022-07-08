# Import required packages
import mysql.connector

# Establish connection to MySQL database
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Phoenix@09871234",
	database="world"
)

# Create a cursor object
my_cursor = mydb.cursor()

# MySQL query fo renaming a table
query = "ALTER TABLE country RENAME to continent"

# Execute the query
my_cursor.execute(query)

# Print names of all tables in the database
my_cursor.execute("SHOW TABLES")
my_result = my_cursor.fetchall()
for row in my_result:
	print(row)

query1 = "DELETE FROM city WHERE FIRST_NAME = 'Taran';"
my_cursor.execute(query1)

# Close database connection
mydb.close()
