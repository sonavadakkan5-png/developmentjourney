# Count how many users are on each platform (Instagram, TikTok, etc.)

import csv

class Mental:

    data : list

    def __init__(self):

        file_path = "inheritance\\mental_health\\mental_health_social_media_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i.get("platform") for i in reader]


    def each_plat(self):

        empty={}

        all_data = [i for i in self.data]

        for i in all_data:

            if i not in empty:

                empty[i]=1

            else:

                empty[i]+=1

        print(empty)

instance = Mental()

instance.each_plat()





