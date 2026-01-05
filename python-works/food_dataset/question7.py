# Count vegetarian vs non-vegetarian dishes.

import csv

class Foods:

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def veg_foods(self):

        veg_foods_only = [i for i in self.data if i.get("diet")=="vegetarian"]

        print(len(veg_foods_only))

    def non_veg(self):

        non_veg_foods_only = [i for i in self.data if i.get("diet")!="vegetarian"]

        print(len(non_veg_foods_only))

food_instance = Foods()

food_instance.veg_foods()

food_instance.non_veg()



