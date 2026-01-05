from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="tripwise_db"
)

curser = connection.cursor()

query="""

insert into user(name,email,password) values(%s,%s,%s)

"""

data =[

    ("sana","sana@gmail.com","sana@123"),
    ("saniya","saniya@gmail.com","saniya@123"),
    ("ambika","ambika@gmail.com","ambika@123"),
    ("arun","arun@gmail.com","arun@123"),
    ("amala","amala@gmail.com","amala@123")
]


curser.executemany(query,data)

connection.commit()

print("query executed.....")

curser.close()

connection.close()

