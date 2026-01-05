# Which country has zero deaths?
import csv

class Covid:

    def __init__(self):

        file_path ="covid_dataset\\country_wise_latest_covid.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def death_rate(self):

        death_rate=[i for i in self.data if i.get("New deaths")=="0"]

        print(death_rate)

covid_instance = Covid()

covid_instance.death_rate()

    
        
        