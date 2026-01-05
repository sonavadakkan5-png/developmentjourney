# Find all products that belong to the brand “Mango”.

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def get_brand(self):

        brands=[(i.get("ID") ,i.get("Category")) for i in self.data if i.get("Brand")=="Mango"]

        print(brands)

instance = Winter()

instance.get_brand()