# Print the Job_Title and Years_Experience of all jobs where Years_Experience is between 10 and 20 years

import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def exp_year(self):

        for row in self.data:

            year = int(row["Years_Experience"])

            if 10<year>20:

                print(f"{row['Job_Title']} : {row['Years_Experience']}")

ai_instance = Aidataset()

ai_instance.exp_year()

