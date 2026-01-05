# Find how many cars have tax > 200

import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_tax(self):

        all_taxs = [i for i in self.data if int(i.get("tax"))>200]

        print(len(all_taxs))

instance = Toyota()

instance.all_tax()

