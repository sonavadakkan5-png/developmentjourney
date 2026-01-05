# 2.Find the post_id with the highest number of likes.

import csv

class Instadata:

    data : list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def example(self):

        all_likes = [int(i.get("likes") )for i in self.data]

        print(all_likes)

        max_all_like = max(all_likes)

        print(max_all_like)

        max_find = [i.get("post_id") for i in self.data if int(i.get("likes"))==max_all_like]

        print(max_find)

insta_instance = Instadata()

insta_instance.example()