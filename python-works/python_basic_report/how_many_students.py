file_path = "python_basic_report\\python_basic_report.csv"

fr = open(file_path,"r")

count =0

import csv

data = csv.DictReader(fr,delimiter="\t")

for i in data:

    count+=1

print(count)

