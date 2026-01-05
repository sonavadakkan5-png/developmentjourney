# Find all dishes that belong to the dessert course.

import csv

class Foods:

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_foods(self):

        desert = [i for i in self.data if i.get("course")=="dessert"]

        print(desert)

food_instance = Foods()

food_instance.all_foods()