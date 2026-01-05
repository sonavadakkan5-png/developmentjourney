# 1. Print the first 5 track names
# Write a program to read the CSV file and print only the first 5 track names.




file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i.get("track_name") for i in reader]


print(data[:6])


