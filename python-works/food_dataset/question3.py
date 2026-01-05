#List all non-vegetarian dishes.

import csv

class Foods:

    def __init__(self):
        
        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [ row for row in reader]

    def non_veg(self):

        non_veg_details = [i.get("name") for i in self.data if i.get("diet")!="vegetarian"]

        print(non_veg_details)

food_instance = Foods()

food_instance.non_veg()