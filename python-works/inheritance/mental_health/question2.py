# Print all users whose daily screen time is more than 400 minutes

import csv

class Mental:

    data :list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def daily_screen(self):

        all_user = [i.get("person_name") for i in self.data if int(i.get("daily_screen_time_min"))>400]

        print(all_user)

instance = Mental()

instance.daily_screen()

