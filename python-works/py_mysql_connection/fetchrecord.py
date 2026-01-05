from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="tripwise_db"
)

curser = connection.cursor()

query = "select * from user"

curser.execute(query)

records = curser.fetchall()

for row in records:

    print(row)

curser.close()

connection.close()