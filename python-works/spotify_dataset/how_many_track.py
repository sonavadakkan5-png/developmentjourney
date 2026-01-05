# 2. Count total rows

# Write a code to count how many total tracks are available in the dataset.


file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [line for line in reader]

print(len(data))

