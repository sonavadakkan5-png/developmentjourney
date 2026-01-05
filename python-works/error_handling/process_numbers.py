file_path = "error_handling\\numss.txt"

try:
    fr = open(file_path,"r")

    new_list = []


    for line in fr:

        line=line.strip()

        try:

            num = int(line)

            new_list.append(num)

        except Exception as e:

            continue

    print(new_list)

    max_num = max(new_list)

    print(max_num)

    min_num = min(new_list)

    print(min_num)

    sum_num = sum(new_list)

    print(sum_num)


    frequent_count = {num:new_list.count(num) for num in new_list}

    f_max = max(frequent_count.values())

    f = [k for k,v in frequent_count.items() if v==f_max]

    print(f)


except Exception as e :

    print(e)




