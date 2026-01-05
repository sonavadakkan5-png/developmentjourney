# 1. Print all food names from the category “Apples”.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [line for line in reader]


all_food_name = [i.get("food_name") for i in data if i.get("category")=="Apples"]

print(all_food_name)


