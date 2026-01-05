# print first 10 records

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]


    def first_ten_records(self):

        print(self.data[:10])

ai_instance = Aidataset()

ai_instance.first_ten_records()




        