# List all patients whose BP > 140.

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_patients_bp(self):

        find_bp = [i for i in self.data if int(i.get("BP")) > 140]

        print(find_bp)

instance = Heart()

instance.all_patients_bp()