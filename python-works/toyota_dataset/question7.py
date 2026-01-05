
# Print all cars where the fuel type is Petrol.

import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_car(self):

        all_cars=[  i.get("model")for i in self.data if i.get("fuelType")=="Petrol"]

        print(all_cars)

instance = Toyota()

instance.all_car()