lst = ["10","20","hello","300","hai","4 00"]

new_list = []


for i in lst:

    try:

        num = int(i)

        new_list.append(num)

    except Exception as e :

        continue

print(new_list)

min_num = min(new_list)

print(min_num)

max_num = max(new_list)

print(max_num)

sum_num = sum(new_list)

print(sum_num)

sort_num = sorted(new_list)

print(sort_num)





    
