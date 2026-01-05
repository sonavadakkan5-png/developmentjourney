file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

total = 0

data = [int(i.get("track_popularity")) for i in reader]

# print(data)

for i in data:

    total+=i

print(total)

len_data = len(data)

print(len_data)

avg = (total/len_data)*100

print(avg)