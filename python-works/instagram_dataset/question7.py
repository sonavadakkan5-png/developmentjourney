# Sort all posts by impressions (descending) and print the top 3.
import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def imp(self):

        impre = [int(i.get("impressions")) for i in self.data ]

        print(sorted(impre,reverse=True)[:3])

insta_instance = Instadata()

insta_instance.imp()

