# Display distinct states present in the dataset.

import csv

class Foods:

    def __init__(self):

        file_path = "food_dataset\\indian_food.csv"

        fr = open(file_path,encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_state(self):

        all_dist_state = [i.get("state") for i in self.data ]

        print(set(all_dist_state))

food_instance = Foods()

food_instance.all_state()