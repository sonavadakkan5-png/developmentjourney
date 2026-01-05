import csv

class Amazon:

    data:list

    def __init__(self):

        file_path = "amazon_sales_dataset\\amazon_sales_2025_INR_cleaned.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def new_data(self):

        metric_1 = [i.get("Metric1") for i in self.data ]

        print(metric_1)

instance = Amazon()

instance.new_data()