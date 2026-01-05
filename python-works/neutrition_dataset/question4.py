# 4. Print food_name and calories for the first 10 foods.

file_path = "neutrition_dataset\\Food_Nutrition_Dataset.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

first_ten_record = data[:11]

for i in first_ten_record:

    foodname = i.get("food_name")

    cal = i.get("calories")

    print(foodname,cal)