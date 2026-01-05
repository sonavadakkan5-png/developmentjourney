# Count unique categories in the dataset.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

all_categories = [i.get("category") for i in data ]

print(len(set(all_categories)))

