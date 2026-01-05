# List patients whose Age > 60 AND Heart Disease = Presence.

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def age_heart(self):

        age_h_d = [i for i in self.data if int ( i.get("Age")) >60 and i.get("Heart Disease")=="Presence"]

        print(age_h_d)

instance = Heart()

instance.age_heart()