from mysql import connector

connection = connector.connect(

    host="localhost",
    user="root",
    password="Password@123",
    database="travel_trip_db"
)

cursor = connection.cursor()

query="""

create table users(
id int primary key auto_increment,
name varchar(100) not null,
email varchar(100) not null unique,
phone varchar(15) not null unique,
created_at datetime default current_timestamp
);


"""

cursor.execute(query)

print("table created...")