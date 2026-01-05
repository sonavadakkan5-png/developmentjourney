# Count how many posts belong to each content category.


import csv

class Instadata:

    data :list

    def __init__(self):

        file_path = "instagram_dataset\\Instagram_Analytics.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [row for row in reader]

    def example(self):

        all_content_cat = [i.get("content_category") for i in self.data ]

        print(all_content_cat)

        empty = {}

        for i in all_content_cat:

            if i not in empty:

                empty[i]=1

            else:

                empty[i]+=1

        print(empty)

        max_find = max(empty.values())

        print(max_find)

        max_cat = {k:v  for k,v in empty.items() if v==max_find}

        print(max_cat)

insta_instance = Instadata()

insta_instance.example()

