# Print the Job_Title and experience of all jobs where Salary > 100000.

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def sal_gt_one_lak(self):

        for row in self.data:

            if int(row["Average_Salary"])>100000:

                print(f"{row['Job_Title']} : {row['Years_Experience']}")

ai_instance = Aidataset()

ai_instance.sal_gt_one_lak()

