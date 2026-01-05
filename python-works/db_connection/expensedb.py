from mysql import connector

class Expenses:

    def __init__(self):

        try:

            self.connection = connector.connect(

                host="localhost",
                user="root",
                password="Password@123",
                database="expense"
            )

            self.cursor = self.connection.cursor()

            print("db connection successfull")
        
        except Exception as e:

            print(e)
    def insert_record(self,**kwargs):

        try:

            column = ""

            values=""

            for k,v in kwargs.items():

                column+=k+","

                values+="%s"+","

            column=column.rstrip(",")

            values=values.rstrip(",")

            query=f"""
                    insert into expense ({column}) values ({values})

            """
            
            data = [v for k,v in kwargs.items() ]

            self.cursor.execute(query,data)

            self.connection.commit()

        except Exception as e:

            print(e)

        print("record inserted....")
    def list_record(self):

        try:

            query="select * from expense"

            self.cursor.execute(query)

            record = self.cursor.fetchall()

            for row in record:

                print(row)

        except Exception as e:

            print(e)
    def specific_id(self,id=None):

        try:

            query="select * from expense where id = %s"

            data = (id,)

            self.cursor.execute(query,data)

            record =self.cursor.fetchone()

            print("one record fetched...")

            print(record)

        except Exception as e:

            print(e)
    def delete_record(self,id=None):
    
        try:

            query="delete from expense where id =%s"

            data =(id,)

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record deleted....")

        except Exception as e:

            print(e)
    def update_record(self,id,**kwargs):
        place_holder = ""

        for k,v in kwargs.items():

            place_holder+=k+"="+"%s"+","

        place_holder=place_holder.rstrip(",")

        query=f"update expense set {place_holder} where  id={id} "

        data = [v for k,v in kwargs.items()]

        self.cursor.execute(query,data)

        self.connection.commit()

expense_instance = Expenses()


expense_instance.update_record(5,name="beena")


expense_instance.list_record()