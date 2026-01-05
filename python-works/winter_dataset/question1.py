# 1. Print the total number of records in the dataset.
import csv
class Winter:

    data : list

    def __init__(self):

        file_path = "winter_dataset\\Winter_Fashion_Trends_Dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]
    @property
    def total_record(self):

        print(len(self.data))

isinstance = Winter()

isinstance.total_record



