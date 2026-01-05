from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="tripwise_db"
)

curser = connection.cursor()

query = " select * from user where id = %s"

data=(2,)

curser.execute(query,data)

records = curser.fetchone()

print(records) 

curser.close()

connection.close()