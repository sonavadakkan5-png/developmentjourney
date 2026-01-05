from mysql import connector

class Feedback:

    def __init__(self):
        
        try:

            self.connection = connector.connect(

                host="localhost",
                user="root",
                password="Password@123",
                database="feedback_db"

            )

            self.cursor = self.connection.cursor()

            print("database connection success")

        except Exception as e:

            print(e)

    def insert_data(self,**kwargs):

        try:

                column=""

                values=""

                for k,v in kwargs.items():

                    column+=k+","

                    values+="%s"+","

                column = column.rstrip(",")

                values=values.rstrip(",")

                query=f"""

                insert into feedback({column}) values({values})

                """

                data = [v for k,v in kwargs.items()]

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted..")

        except Exception as e:

            print(e)

    def list_feedback(self):
         
        try:
              
            query = "select * from feedback "

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                 
                print(row)
        except Exception as e:
             
             print(e)

    def fetch_id(self,id=None):
         
        try:
              
            query="select * from feedback where id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:
             
            print(e)


    def delete_records(self,id=None):

        try:

            query="delete from feedback where id =%s"

            data=(id,)

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted")

        except Exception as e :

            print(e)       



feddback_instance = Feedback()

feddback_instance.insert_data(name="sona",email="sona@gmail.com",rating=4,comments="good")

feddback_instance.list_feedback()

feddback_instance.fetch_id(2)

feddback_instance.delete_records(3)


