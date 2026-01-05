# Print all post_ids where the media_type is “Reel”

import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def media(self):

        media_type = [i.get("post_id") for i in self.data if i.get("media_type")=="Reel"]

        print(media_type)

insta_instance = Instadata()

insta_instance.media()