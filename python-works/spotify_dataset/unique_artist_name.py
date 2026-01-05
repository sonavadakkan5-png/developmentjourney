
# 3. List all unique artist names

# Print all unique artists from the dataset.

file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = {line.get("artist_name",0)for line in reader}

print(data)