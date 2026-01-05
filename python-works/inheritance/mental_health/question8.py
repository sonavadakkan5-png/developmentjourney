# unique names

import csv

class Mental:

    data :list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def unique(self):

        unique_data = [i.get("person_name") for i in self.data]

        print(set(unique_data))

isinstance = Mental()

isinstance.unique()