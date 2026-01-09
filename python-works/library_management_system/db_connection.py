from mysql import connector

class Library:

    def __init__(self):
        
        try:
            
            self.connection = connector.connect(

                host="localhost",

                user="root",

                password="Password@123",

                database="library_db"
            )

            self.cursor =self.connection.cursor()

            print("database connection ok")

        except Exception as e:

            print(e)

    def add_library(self,**kwargs):

        try:
                column=""

                values=""

                for k,v in kwargs.items():
                     
                     column+=k+","

                     values+="%s"+","

                column = column.rstrip(",")

                values=values.rstrip(",")

                query=f"""

                insert into library({column}) values({values})

                """

                data = [v for k,v in kwargs.items()]

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted..")

        except Exception as e:
             
             print(e)

    def list_library(self):
         
        try:
              
            query = "select * from library "

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                 
                print(row)
        except Exception as e:
             
             print(e)

    def fetch_id(self,id=None):
         
        try:
              
            query="select * from library where id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:
             
            print(e)

    def delete_records(self,id=None):

        try:

            query="delete from library where id =%s"

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

        query=f"update library set {place_holder} where  id={id} "

        data = [v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()

            
instance = Library()

# instance.add_library(member_name="athira", book_name="night walk",author="sarala",status="issued")

instance.list_library()



# instance.update_record(id=3,member_name="sooraj")

instance.delete_records(3)

instance.fetch_id(1)


            