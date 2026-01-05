# Find all cars priced between 15,000 and 20,000.

import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_cars(self):

        all_car = [i for i in self.data if int(i.get("price")) > 15000 and int (i.get("price"))<20000]

        print(all_car)

isinstance = Toyota()

isinstance.all_cars()
