# Print all unique Job Titles in the dataset.

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def unique_data(self):

        unique_set = set()

        for row in self.data:

            unique_set.add(row["Job_Title"])

        for title in unique_set:

            print(title)

ai_instance = Aidataset()

ai_instance.unique_data()

