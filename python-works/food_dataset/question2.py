#print all vegitarian dishes
import csv

class Foods:

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_veg(self):

        veg_only = [i.get("name") for i in self.data if  i.get("diet")=="vegetarian"]

        print(veg_only)

food_instance = Foods()

food_instance.all_veg()
