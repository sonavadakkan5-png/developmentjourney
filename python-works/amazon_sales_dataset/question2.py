# Report_Section =COD_VS_DIGITAL_PAYMENTS

import csv

class Amazon:

    data:list

    def __init__(self):

        file_path = "amazon_sales_dataset\\amazon_sales_2025_INR_cleaned.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row  for row in reader]

    def filter_record(self):

        report_section = [ i for i in self.data if i.get("\ufeffReport_Section")=="COD_VS_DIGITAL_PAYMENTS"]

        print(report_section)

        print(len(report_section))

am_instance = Amazon()

am_instance.filter_record()


