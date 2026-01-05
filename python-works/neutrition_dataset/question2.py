# 2. Count how many food items belong to “Cakes and pies”.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

all_category = [i for i in data if i.get("category")=="Cakes and pies"]

print(len(all_category))

