import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'Gvinay@1',
    port='3306',
    database='vinaydb'
)
mycurs = mydb.cursor()

#mycurs.execute("CREATE TABLE Person(name VARCHAR(50),age smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT)")
#mycurs.execute("INSERT INTO Person(empname, empage) VALUES (%S,%S)",("kumar",19))
#mydb.commit()

mycurs.execute("SELECT *FROM table1")
for x in mycurs:
    print(x)