# Print the total number of rows in the dataset.

import csv

class Mental:

    data : list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_row(self):

        total_row = [i for i in self.data]

        print(len(total_row))

isinstance = Mental()

isinstance.all_row()


        
        