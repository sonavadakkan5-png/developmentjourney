# Find dishes where prep_time = -1.

import csv

class Foods:

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_foods(self):

        prep_time = [i.get("name") for i in self.data if i.get("prep_time")=="-1"]

        print(prep_time)

food_instance = Foods()

food_instance.all_foods()