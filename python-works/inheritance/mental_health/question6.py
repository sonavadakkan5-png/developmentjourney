# Find all users where screen_time > 300 AND sleep_hours < 7

import csv

class Mental:

    data :list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_user(self):

        all_users = [ i for i in self.data if int( i.get("daily_screen_time_min"))>300 and float(i.get("sleep_hours"))<7]

        print(all_users)

instance = Mental()

instance.all_user()