# How many total confirmed cases are reported in India?

import csv

class Covid:

    data :list

    def __init__(self):

        file_path="covid_dataset//country_wise_latest_covid.csv"

        fr =open(file_path,"r",encoding="utf-8")

        reader=csv.DictReader(fr)

        self.data = [row for row in reader]
        
    def india_cases(self):

        total_case_india = [i.get("Confirmed") for i in self.data if i.get("Country/Region")=="India"]

        print(total_case_india)

covid_instance = Covid()

covid_instance.india_cases()