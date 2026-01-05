# How many patients have Heart Disease = Absence?

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def heart_disease(self):

        heart_d = [i for i in self.data if i.get("Heart Disease")=="Absence"]

        print(heart_d)

        print(len(heart_d))

instance = Heart()

instance.heart_disease()