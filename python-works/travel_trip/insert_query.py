from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="travel_trip_db"
)

cursor = connection.cursor()

query="""

insert into users (name, email, phone)values(%s,%s,%s)

"""

data = [
('Sona Vadakkan', 'sona@gmail.com', '9876543210'),
('Anil Kumar', 'anil@gmail.com', '9123456789'),
('Rahul Das', 'rahul@gmail.com', '9988776655'),
('Meera Nair', 'meera@gmail.com', '9012345678'),
('Akhil Raj', 'akhil@gmail.com', '9090909090')
]

cursor.executemany(query,data)

connection.commit()

print("query executed.....")

cursor.close()

connection.close()

