# 2. Print all unique brands.
import csv

class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    @property
    
    def get_unique(self):

        all_brand = [i.get("Brand") for i in self.data ]

        print(set(all_brand))

isinstance = Winter()

isinstance.get_unique