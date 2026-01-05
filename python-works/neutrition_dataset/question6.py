# Find the highest calorie food and print its name,category,fat value.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

all_cal = [ float(i.get("calories")) for i in data]

# print(all_cal)

highest_cal = max(all_cal)

print(highest_cal)

for i in data:

    if float(i.get("calories")) == highest_cal:

        print(i["food_name"])

        print(i["category"])

        print(i["fat"])





