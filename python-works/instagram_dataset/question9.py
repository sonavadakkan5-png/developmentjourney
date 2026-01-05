# Which post gained the highest followers

import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def follow(self):

        followers = [int(i.get("followers_gained")) for i in self.data ]

        max_val = max(followers)


        f_p = [i["post_id"] for i in self.data if  int(i.get("followers_gained"))==max_val]

        print(f_p)

insta_instance = Instadata()

insta_instance.follow()


