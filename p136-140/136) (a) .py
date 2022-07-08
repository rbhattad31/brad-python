# Import required module
import mysql.connector

# Establish connection
# to MySQL database
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Phoenix@09871234",
	database="world")

# Create cursor object
my_cursor = mydb.cursor()

# Execute query
query = "SELECT table_name AS `Table`, \
		round(((data_length + index_length) \
		/ 1024 / 1024), 2) `Size in MB` \
		FROM information_schema.TABLES \
		WHERE table_schema = 'world' AND \
		table_name = 'city';"

my_cursor.execute(query)

# Display size of each table
my_result = my_cursor.fetchall()

for item in my_result:
    print(item[0],"Size in MB:",item[-1])