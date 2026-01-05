# Print the highest and lowest mileage.
import csv

class Toyota:

    data : list

    def __init__(self):
        
        file_path = "toyota_dataset\\toyota.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_mileage(self):

        all_mil = [i.get("mileage") for i in self.data]

        min_mil = min(all_mil)

        max_mil =max(all_mil)

        print(min_mil)

        print(max_mil)

instance = Toyota()

instance.all_mileage()



