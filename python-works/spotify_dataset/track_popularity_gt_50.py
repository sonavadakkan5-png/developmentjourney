file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

tn = [i.get("track_name") for i in reader if int(i.get("track_popularity"))>50]

print(tn)