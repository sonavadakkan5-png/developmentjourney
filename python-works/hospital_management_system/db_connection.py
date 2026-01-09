from mysql import connector

class Hospital:

    def __init__(self):

        try:
        
            self.connection = connector.connect(

                host="localhost",
                user="root",
                password="Password@123",
                database="hospital_db"
            )

            self.cursor = self.connection.cursor()

            print("data base connection ok....")

        except Exception as e:

            print(e)

    def add_details(self,**kwargs):

        try:
                column=""

                values=""

                for k,v in kwargs.items():
                     
                     column+=k+","

                     values+="%s"+","

                column = column.rstrip(",")

                values=values.rstrip(",")

                query=f"""

                insert into hospital({column}) values({values})

                """

                data = [v for k,v in kwargs.items()]

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted..")

        except Exception as e:
             
             print(e)

    def list_details(self):
         
        try:
              
            query = "select * from hospital "

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                 
                print(row)
        except Exception as e:
             
             print(e)

    def fetch_id(self,id=None):
         
        try:
              
            query="select * from hospital where patient_id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:
             
            print(e)

    def delete_records(self,id=None):

        try:

            query="delete from hospital where patient_id =%s"

            data=(id,)

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted")

        except Exception as e :

            print(e)

    def update_record(self,patient_id,**kwargs):

        place_holder = ""

        for k,v in kwargs.items():

            place_holder+=k+"="+"%s"+","

        place_holder=place_holder.rstrip(",")

        query=f"update hospital set {place_holder} where  patient_id={id} "

        data = [v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()

        

instance = Hospital()

# instance.add_details(patient_name="sneha",age=35,gender="Female",phone="1478545777",address="mangalath",doctor_name="suma")

# instance.list_details()

# instance.fetch_id(1)

instance.delete_records(4)

instance.update_record(doctor_name="murali",patient_id=1)