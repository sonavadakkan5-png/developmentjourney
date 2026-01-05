# Calculate the average MPG.

import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_mpg(self):

        all_mpg = [float(i.get("mpg")) for i in self.data ]

        total = len(all_mpg)

        sum1 = sum(all_mpg)

        avg = (sum1/total)

        print(avg)

isinstance = Toyota()

isinstance.all_mpg()

