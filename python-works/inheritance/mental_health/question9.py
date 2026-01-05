# Print all Female users.

import csv

class Mental:

    data :list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def female_user(self):

        all_f = [i.get("person_name") for i in self.data if i.get("gender")=="Female"]

        print(all_f)

instance = Mental()

instance.female_user()