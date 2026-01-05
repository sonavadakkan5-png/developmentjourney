# 3. Print all foods with calories less than 100.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

all_calories = [i.get("food_name") for i in data if float (i.get("calories"))<100]

print(all_calories)

print(len(all_calories))

