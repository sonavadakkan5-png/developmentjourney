# Count how many male (Sex = 1) and female (Sex = 0) patients are there.

import csv

class Heart:

    data : list

    def __init__(self):

        file_path = "heart_dataset\\Heart_Disease_Prediction.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def count_male(self):

        male_count = [i for i in self.data if int(i.get("Sex"))==1]

        print(male_count)

        print(len(male_count))

    def count_female(self):

        female_count = [i for i in self.data if int(i.get("Sex"))==0]

        print(female_count)

        print(len(female_count))

instance = Heart()

instance.count_female()

instance.count_male()