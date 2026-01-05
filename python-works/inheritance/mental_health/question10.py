# Print all users whose positive_interactions_count > negative_interactions_count.

import csv

class Mental:

    data :list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_user(self):
    
        da_ta = [i.get("person_name") for i in self.data if int(i.get("positive_interactions_count")) > int(i.get("negative_interactions_count") )]

        print(da_ta)
        

instance = Mental()

instance.all_user()