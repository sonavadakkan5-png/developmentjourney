import csv

class Amazon:

    data:list

    def __init__(self):

        file_path = "amazon_sales_dataset\\amazon_sales_2025_INR_cleaned.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def CUSTOMER_COUNT_BY_STATE_s(self):

        all_details=[i.get("Dimension") for i in self.data ]

        print(all_details)

        # print(self.data[0].keys())

instance = Amazon()

instance.CUSTOMER_COUNT_BY_STATE_s()