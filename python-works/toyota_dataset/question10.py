# Print all unique engine sizes.

import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_unique(self):

        all_uniques = [ i.get("engineSize")for i in self.data]

        print(set(all_uniques))

instance = Toyota()

instance.all_unique()