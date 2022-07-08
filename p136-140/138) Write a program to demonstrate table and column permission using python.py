# import required module
import pymysql

# establish connection to MySQL
connection = pymysql.connect(

    # specify host
    host='localhost',

    # specify root account
    user='root',

    # specify password for root account
    password='Phoenix@09871234',

    # default port number is 3306 from MySQL
    port=3306
)

# make a cursor to run sql queries
my_cursor = connection.cursor()

# granting all permissions on all databases and their
# tables of root user permission also includes
# table and column grants
my_cursor.execute("Grant all on *.* to root@localhost")

# print all privileges of root user
my_cursor.execute("Show grants for root@localhost")
result = my_cursor.fetchall()
print(result)

# commit privileges
my_cursor.execute("Flush Privileges")

# close connection to MySQL
connection.close()
