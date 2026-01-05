file_path = "cart\\cart_items_100.csv"

fr = open(file_path,"r",encoding="utf-8")

import csv 

reader = csv.DictReader(fr)

data = [row for row in reader]

# print(data)


order_summary = {}

for i in data:

    title = i.get("title")

    qt = int(i.get("quantity"))

    if title not in order_summary:

        order_summary[title]=qt

    else:

        order_summary[title]+=qt

# print(order_summary)


min_number = min(order_summary.values())

# print(min_number)

max_number = max(order_summary.values())

# print(max_number)

min_val = {k:v for k,v in order_summary.items() if v==min_number}

# print(min_val)

max_val = {k:v for k,v in order_summary.items() if v==max_number}

# print(max_val)



user_dict = {}

for i in data:

    all_user = i.get("user")

    # print(all_user)

    if all_user not in user_dict:

        user_dict[all_user]=1

    else:

        user_dict[all_user]+=1

# print(user_dict)



max_user = max(user_dict.values())

print(max_user)

user_count = {k:v for k,v in user_dict.items() if v==max_user}

print(user_count)





