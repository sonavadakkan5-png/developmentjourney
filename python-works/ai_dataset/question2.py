# 2. for each person ,if the year of experience >28 then print their educational level and title

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def year_ex(self):

        for row in self.data:

            if int(row["Years_Experience"])>28:

                print(f"{row['Job_Title']} : {row['Education_Level']}")

ai_instance = Aidataset()

ai_instance.year_ex()

