from mysql import connector

class Vehicle:
 
    def __init__(self):
        
        try:

            self.connection = connector.connect(

                host="localhost",
                user="root",
                password="Password@123",
                database="gosell_db"
            )

            self.cursor = self.connection.cursor()

            print("database connection success")

        except Exception as e:

            print(e)

    def add_vehicle(self,**kwargs):

        try:
                column=""

                values=""

                for k,v in kwargs.items():
                     
                     column+=k+","

                     values+="%s"+","

                column = column.rstrip(",")

                values=values.rstrip(",")

                query=f"""

                insert into vehicle({column}) values({values})

                """

                data = [v for k,v in kwargs.items()]

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted..")

        except Exception as e:
             
             print(e)

    def list_vehicle(self):
         
        try:
              
            query = "select * from vehicle "

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                 
                print(row)
        except Exception as e:
             
             print(e)

    def fetch_id(self,id=None):
         
        try:
              
            query="select * from vehicle where id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:
             
            print(e)

    def delete_records(self,id=None):

        try:

            query="delete from vehicle where id =%s"

            data=(id,)

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted")

        except Exception as e :

            print(e)

    def update_record(self,id,**kwargs):

        place_holder = ""

        for k,v in kwargs.items():

            place_holder+=k+"="+"%s"+","

        place_holder=place_holder.rstrip(",")

        query=f"update vehicle set {place_holder} where  id={id} "

        data = [v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()

        



vehicle_instance = Vehicle()

# vehicle_instance.add_vehicle(name="maruthi",price=12450,year="2024",fuel_type="ev",comments="good condition",running_km=12000,owner_type="single",owner="bharath",location="kkm")

vehicle_instance.list_vehicle()

# vehicle_instance.fetch_id(3)

vehicle_instance.delete_records(13)

vehicle_instance.update_record(4,name="toyota")



