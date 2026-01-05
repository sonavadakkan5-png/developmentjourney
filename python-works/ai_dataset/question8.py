# Print all jobs where Automation_Risk is above 70%

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def all_jobs(self):

        for row in self.data:

            if float(row["Automation_Probability_2030"]) > 0.70:

                print(f"{row['Job_Title']}")

all_job_instance1 = Aidataset()

all_job_instance1.all_jobs()

