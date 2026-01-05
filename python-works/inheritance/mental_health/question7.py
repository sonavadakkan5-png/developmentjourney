# Print top 5 people with highest daily_screen_time_min.

import csv

class Mental:

    data :list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def highest(self):

        all_user =sorted ({int(i.get("daily_screen_time_min")) for i in self.data},reverse=True)

        print(all_user[:5])

isinstance = Mental()

isinstance.highest()