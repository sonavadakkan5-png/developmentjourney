# Find the most expensive product for each brand.

import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def price_map(self):

        empty = {}

        for i in self.data:

            product =i.get("Category")
            
            price=float(i.get("Price(USD)"))

            brand =i.get("Brand")

            if brand not in empty:

                empty[brand]=(product,price)

            else:

                if price > empty[brand][1]:

                    empty[brand]=(product,price)

        print(empty)

isinstance = Winter()

isinstance.price_map()