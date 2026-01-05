# print only the ingredients is oil

import csv

class Foods:

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_food(self):

        all_foods = [ i.get("ingredients") for i in self.data]

        empty = []

        for i in all_foods:

            if "oil" in i:

                empty.append(i)

                print(empty)
food_instance = Foods()

food_instance.all_food()

            
