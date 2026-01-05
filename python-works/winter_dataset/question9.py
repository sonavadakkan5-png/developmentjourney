# List all “Coat” category items sorted by price (high→ low).

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def cat_item(self):

        list_all=sorted([i.get("Price(USD)") for i in self.data  if i.get("Category")=="Coat"],reverse=True)

        print(list_all)

isinstance = Winter()

isinstance.cat_item()