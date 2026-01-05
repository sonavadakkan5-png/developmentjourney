# Calculate the average daily_screen_time_min.

import csv

class Mental:

    data : list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def screen_time(self):

        daily_scrren = [int(i.get("daily_screen_time_min")) for i in self.data]

        total_sum=sum(daily_scrren)

        len_f = len(daily_scrren)

        print((total_sum/len_f)*100)

constructor = Mental()

constructor.screen_time()

