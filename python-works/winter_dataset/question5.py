# Count how many products are made of “Leather”

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def get_products(self):

        made_l = [i for i in self.data  if i.get("Material")=="Leather"]

        print(len(made_l))

instance = Winter()

instance.get_products()

