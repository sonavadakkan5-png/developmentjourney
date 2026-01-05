from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="travel_trip_db"
)

cursor = connection.cursor()

query = "update users set name=%s, email=%s where id=%s"

data=("akhilrajan","akhilrajan@gmail.com",5)

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()