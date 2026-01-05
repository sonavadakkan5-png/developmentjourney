# 1. Print the total number of posts in the dataset.

import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def insta(self):

        print(len(self.data))

insta_instance = Instadata()

insta_instance.insta()
