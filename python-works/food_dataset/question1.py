# how many records are there

import csv

class Foods:

    data : list

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data=[row for row in reader]

    def total_record(self):

        total_records = [i for i in self.data]

        print(len(total_records))

food_instance = Foods()

food_instance.total_record()

