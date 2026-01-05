file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [line.get("explicit") for line in reader]

exp_true = data.count("TRUE")

print(exp_true)