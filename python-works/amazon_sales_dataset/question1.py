# how many records are there

import csv

class Amazon:

    data:list

    def __init__(self):

        file_path = "amazon_sales_dataset\\amazon_sales_2025_INR_cleaned.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def total_record(self):

        total_records = [i for i in self.data]

        print(len(total_records))

am_instance = Amazon()

am_instance.total_record()

