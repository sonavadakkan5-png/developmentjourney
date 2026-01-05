file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [line for line in reader]

all_data = [i for i in data ]

print(data[:10])