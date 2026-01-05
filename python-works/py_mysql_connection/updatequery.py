from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="tripwise_db"
)

cursor = connection.cursor()

query = "update user set name=%s, password=%s where id=%s"

data=("saniyakk","saniyakk@123",3)

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()