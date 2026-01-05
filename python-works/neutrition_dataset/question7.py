# For each category, print how many food items it has, and highest value of that food items also print their name .

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

all_cat = {}

for i in data:

    cat = i.get("category")

    if cat not in all_cat:

        all_cat[cat]=1

    else:

        all_cat[cat]+=1

print(all_cat)

hi = max(all_cat.values())

print(hi)

h = {k:v for k,v in all_cat.items() if v == hi}

print(h)

