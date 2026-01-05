from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="travel_trip_db"
)

curser = connection.cursor()

query = " delete from users where id = %s"

data=(2,)

curser.execute(query,data)

connection.commit()

print("record deleted") 

curser.close()

connection.close()