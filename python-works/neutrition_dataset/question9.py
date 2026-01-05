# Print all foods where protein > 5 and fat < 5.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [line for line in reader]

all_foods = [ i.get("food_name")for i in data if float (i.get("protein",0))> 5 and float(i.get("fat",0))<5]

print(all_foods)