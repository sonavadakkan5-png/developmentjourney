# Count how many products belong to each season (Winter 2023/2024/2025)


import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_count(self):

        empty ={}

        for i in self.data:

            season = i.get("Season")

            if season not in empty:

                empty[season]=1

            else:

                empty[season]+=1


        print(empty)

isinstance = Winter()

isinstance.all_count()

