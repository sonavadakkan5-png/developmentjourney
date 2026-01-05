# Find media_type where likes > 190000


import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def like(self):

        all_likes = [ i.get("media_type") for i in self.data if int( i.get("likes"))>190000]

        print(all_likes)

insta_instance = Instadata()

insta_instance.like()

