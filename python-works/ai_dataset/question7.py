# Count the number of jobs that require a Master’s degree.

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def count_education_levels(self):

        edu_count = {}

        for row in self.data:

            edu = row["Education_Level"]

            if edu in edu_count:

                edu_count[edu] += 1
            else:
                edu_count[edu] = 1

        for k,v in edu_count.items():

            print(f"{k}: {v}")

ai_instance = Aidataset()

ai_instance.count_education_levels()

