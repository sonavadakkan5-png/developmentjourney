file_path = "own_works\\cities.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv

reader = csv.DictReader(fr)

data = [i for i in reader]

first_five_city_name = [i.get("city_name") for i in data[-5:]]

# print(first_five_city_name)

all_country = [i.get("country") for i in data]

unique = set(all_country)

# print(list(unique))

condition = [i.get("city_name") for i in data if i.get("country")=="Sri Lanka"]

# print(condition)

dictt = {}

for i in condition:

    if i not in dictt:

        dictt[i]=1

    else:

        dictt[i]+=1

# print(dictt)


longti = [float(i.get("longitude")) for i in data]

# print(longti)

max_val = max(longti)

# print(max_val)



city_contry = [f"{i.get("city_name")}- {i.get("country")}" for i in data]

# print(city_contry)

empty= {}

for i in city_contry:

    if i not in empty:

        empty[i]=1

    else:

        empty[i]+=1

# print(empty)


city_name = [i.get("city_name") for i in data]

print(sorted(city_name,reverse=True))