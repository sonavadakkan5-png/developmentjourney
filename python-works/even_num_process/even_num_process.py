file_path= "even_num_process\\even_numbers_process.txt"

fr =open(file_path,"r",encoding="utf-8")

all_num=[]

for line in fr:

    line=line.strip()

    try:

        line = int(line)

        all_num.append(line)

    except Exception as e:

        continue

print(all_num)

even_num = []

for i in all_num:

    if i%2==0:

        even_num.append(i)

print(even_num)


dictt ={i:even_num.count(i) for i in even_num}

print(dictt)


max_count= max(dictt.values())

print(max_count)

max_c ={k:v for k,v in dictt.items() if v==max_count}

print(max_c)