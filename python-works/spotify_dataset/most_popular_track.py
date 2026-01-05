file_path = "spotify_dataset\\spotify_data_process.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [row for row in reader]

pop = {}

for i in data:

    track_name = i.get("track_name")

    track_popularity=i.get("track_popularity")

    if track_name not in pop:

        pop[track_name]=track_popularity

    else:

        pop[track_name]+=track_popularity

# print(pop)

max_v = max(pop.values())

print(max_v)


c = [k for k,v in pop.items() if v==max_v]

print(c)