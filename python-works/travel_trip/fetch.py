from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="travel_trip_db"
)

curser = connection.cursor()

query = "select * from users"

curser.execute(query)

records = curser.fetchall()

for row in records:

    print(row)

curser.close()

connection.close()