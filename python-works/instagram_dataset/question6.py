# Find posts that reached more than 1 million impressions.
import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def imp(self):

        impre = [i.get("post_id") for i in self.data if int (i.get("impressions"))>1000000]

        print(impre)

insta_instance = Instadata()

insta_instance.imp()