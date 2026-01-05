# Compare the average reach of Photos vs Reels.
import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_p(self):

        all_photos = [i for i in self.data if i.get("media_type")=="Photo"]

        all_reels = [i for i in self.data if i.get("media_type")=="Reel"]

        post_count = len(all_photos)

        reels_count = len(all_reels)

        avg_p = sum(int(i["reach"]) for i in all_photos) / len(all_photos)

        avg_r = sum(int(i["reach"]) for i in all_reels) / len(all_reels)


        print(avg_p)

        print(avg_r)

insta_instance = Instadata()

insta_instance.all_p()
