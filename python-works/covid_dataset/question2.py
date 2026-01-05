# Which country has the highest number of deaths?
import csv

class Covid:

    def __init__(self):
        
        file_path="covid_dataset//country_wise_latest_covid.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader= csv.DictReader(fr)

        self.data=[row for row in reader]

    def highest_death_rate(self):

        count_death_rate=[int(i.get("Deaths")) for i in self.data]

        print(max(count_death_rate))

covid_instance = Covid()

covid_instance.highest_death_rate()

