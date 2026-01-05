# List all unique media types

import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def all_type(self):

        all_media_type = [i.get("media_type") for i in self.data]

        unique = set(all_media_type)

        print(list(unique))

instagram_instance = Instadata()

instagram_instance.all_type()

