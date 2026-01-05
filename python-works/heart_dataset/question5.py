# Find the average age of all patients.

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def find_avg(self):

        find_avgs = [int(i.get("Age")) for i in self.data]

        find_sum = sum(find_avgs)

        avg_find = find_sum/len(find_avgs)

        print(avg_find)

instance = Heart()

instance.find_avg()
