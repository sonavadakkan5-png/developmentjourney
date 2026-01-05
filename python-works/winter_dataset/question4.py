# Print all products with price less than 200 USD

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def get_price(self):

        all_price = [ i.get("Category") for i in self.data if i.get("Price(USD)")]

        print(all_price)

instance = Winter()

instance.get_price()