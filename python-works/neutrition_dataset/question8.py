# Sort the foods by protein content (highest first). Print top 5.


file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [line for line in reader]

protein = [float(i.get("protein"))for i in data ]

max_pro = max(protein)

print(max_pro)

so = sorted(protein,reverse="True")

print(so)