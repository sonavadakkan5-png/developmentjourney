# Print the Tech_Growth_Factor and Risk_Category of all jobs where Education_Level is "Bachelor's Degree"


import csv

class Aidataset:

    data:list

    def __init__(self):

        file_path = "ai_dataset\\AI_Impact_on_Jobs_2030.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def ba_degree(self):

        for row in self.data:

            if row["Education_Level"]=="Master's":

                print(f"{row['Tech_Growth_Factor']} : {row['Risk_Category']}")

ai_instance = Aidataset()

ai_instance.ba_degree()



