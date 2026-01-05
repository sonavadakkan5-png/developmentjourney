# Find all items where popularity score is greater than 8

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def popularity(self):

        popularity = [i  for i in self.data if float(i.get("Popularity_Score"))>8]

        print(popularity)

isinstance = Winter()

isinstance.popularity()










    




