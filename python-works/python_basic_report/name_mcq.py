file_path = "python_basic_report\\python_basic_report.csv"

fr = open(file_path,"r")

import csv

data = csv.DictReader(fr,delimiter="\t")

for row in data:

    name = row["NAME"].strip()

    mcq = row["MCQ1"].strip()

    print(name,mcq)