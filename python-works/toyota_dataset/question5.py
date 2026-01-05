# Sort all cars by price (ascending and descending)


import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_price(self):

        all_prices =sorted([int(i.get("price")) for i in self.data],reverse=True) 

        print(all_prices)

instance = Toyota()

instance.all_price()