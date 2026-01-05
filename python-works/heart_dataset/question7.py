# Find the minimum and maximum heart rate (Max HR).

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def find_heart_rate(self):

        maximum_rate = [int(i.get("Max HR") )for i in self.data]

        print(max(maximum_rate))

        print(min(maximum_rate))

instance = Heart()

instance.find_heart_rate()