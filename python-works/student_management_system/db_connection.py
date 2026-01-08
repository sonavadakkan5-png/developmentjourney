from mysql import connector

class studentdb:

    def __init__(self):
        
        try:
            
            self.connection = connector.connect(

                host="localhost",

                user="root",

                password="Password@123",

                database="student_management_db"
            )

            self.cursor =self.connection.cursor()

            print("database connection ok")

        except Exception as e:

            print(e)

    def add_student(self,**kwargs):

        try:
                column=""

                values=""

                for k,v in kwargs.items():
                     
                     column+=k+","

                     values+="%s"+","

                column = column.rstrip(",")

                values=values.rstrip(",")

                query=f"""

                insert into student({column}) values({values})

                """

                data = [v for k,v in kwargs.items()]

                self.cursor.execute(query,data)

                self.connection.commit()

                print("record inserted..")

        except Exception as e:
             
             print(e)

    def list_student(self):
         
        try:
              
            query = "select * from student "

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                 
                print(row)
        except Exception as e:
             
             print(e)

    def fetch_id(self,id=None):
         
        try:
              
            query="select * from student where id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            records = self.cursor.fetchone()

            print(records)

        except Exception as e:
             
            print(e)

    def delete_records(self,id=None):

        try:

            query="delete from student where id =%s"

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

        query=f"update student set {place_holder} where  id={id} "

        data = [v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()


instance = studentdb()

# instance.add_student(name="arun",email="arun@gmail.com",phone="45784512458",course="msc")

instance.list_student()

instance.fetch_id()



