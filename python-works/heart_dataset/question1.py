# How many total records (patients) are there in the dataset?

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_record(self):

        all_record_print = [i for i in self.data]

        print(len(all_record_print))

instance = Heart()

instance.all_record()