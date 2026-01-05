# how many rows in the dataset
import csv

class Toyota:

    data :list

    def __init__(self):

        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]
    @property
    def total_row(self):

        rows = [i for i in self.data]

        print(len(rows))


instance = Toyota()

instance.total_row
