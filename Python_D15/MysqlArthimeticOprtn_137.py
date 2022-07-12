import mysql.connector

conn = mysql.connector.connect(
        user='root',
        host='127.0.0.1',
        database='python',
        port='3307'
    )
mycursor = conn.cursor(dictionary=True)
# Adding

query = "SELECT price, \
                GST, \
                concat(price + GST) AS 'selling price' \
         FROM items"

# subtraction
query = "SELECT price, \
               GST, \
                concat(price - GST) AS 'selling price' \
         FROM items"

# multiplication
query = "SELECT price, \
               GST, \
                concat(price * GST) AS 'selling price' \
         FROM items"

# Execute the query
mycursor.execute(query)
# Fetch result of query
result = mycursor.fetchall()

# Print result of query
print(f"SP \t gst \t Sale Amount")

for row in result:
    # Each value printed for display purpose (you can simply print row)
    print(f"{row['price']} \t {row['GST']} \t {row['selling price']}")

conn.close()
