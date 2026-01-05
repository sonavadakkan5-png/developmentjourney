# Count cars with mileage less than 10,000 km.

import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_car(self):

        all_cars = [i for i in self.data if int(i.get("mileage"))>10000]

        print(len(all_cars))

isinstance= Toyota()

isinstance.all_car()