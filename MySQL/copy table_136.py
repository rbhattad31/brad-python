import mysql.connector

# check connection
connection = mysql.connector.connect(host='localhost', database='Demo_1', user='root', password='********')
cursor = connection.cursor()

# copy a table
Db = 'Demo_1'
Tb_1 = 'employee'
Tb_2 = 'employee_2'
Query = "CREATE TABLE {} SELECT * FROM {}".format(Tb_2, Tb_1)

# Get Size
Query = "SELECT  table_name AS 'Table',  round(((data_length + index_length) / 1024 / 1024), 2) `Size in MB` FROM information_schema.TABLES WHERE table_schema = {} AND table_name = {}".format(Db, Tb_1)
cursor.execute(Query)
result = cursor.fetchall()
for item in result:
    print(item[0], "Size in MB: ", item[-1])

# Rename Table
Query = "RENAME TABLE {} to {}".format(Tb_1, 'employee_1')
cursor.execute(Query)

# Delete Element
query = " DELETE FROM {}  WHERE EMP_Name = 'Blue'".format(Tb_1)
cursor.execute(query)

# close DB
cursor.commit()
cursor.close()