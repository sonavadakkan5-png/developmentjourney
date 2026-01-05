# How many patients have Exercise angina = 1?

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def exercise(self):

        exercises = [i for i in self.data if int( i.get("Exercise angina"))==1]

        print(exercises)

instance = Heart()

instance.exercise()