# Find how many cars are from each year.
import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_year(self):

        all_yr = [i.get("year") for i in self.data]

        empty = {}

        for i in all_yr:

            if i not in empty:

                empty[i]=1

            else:

                empty[i]+=1

        print(empty)

isinstance = Toyota()

isinstance.all_year()