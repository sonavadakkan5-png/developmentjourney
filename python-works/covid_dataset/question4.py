# Display countries with New cases > 10,000.
import csv

class Covid:

    def __init__(self):

        file_path="covid_dataset\\country_wise_latest_covid.csv"

        fr=open(file_path,"r",encoding="utf-8")

        reader=csv.DictReader(fr)

        self.data=[row for row in reader]

    def new_case(self):

        new_cases=[i.get("Country/Region") for i in self.data if  int(i.get("New cases"))>10000]

        print(new_cases)

covid_instance = Covid()

covid_instance.new_case()
        
        