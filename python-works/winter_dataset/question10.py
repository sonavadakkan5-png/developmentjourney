# Find all products that are both “Luxury” style and priced above 500 USD.

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_data(self):

        all_product = [i for i in self.data if i.get("Style")=="Luxury" and float(i.get("Price(USD)"))>500]

        print(all_product)

isinstance = Winter()

isinstance.all_data()