file_path = "titanic\\dataset.csv"

fr = open(file_path,"r")

import csv

data = csv.DictReader(fr)

li = [i for i in data]

dictt = [dic.get("Name") for dic in li]

gender = [p.get("Sex") for p in li]

male_count = gender.count("male")

female_count = gender.count("female")

# print("male",male_count)

# print("female",female_count)

survival_ct = [i.get("Survived") for i in li]

one_ct = survival_ct.count("1")

zero_ct = survival_ct.count("0")

# print(one_ct)

# print(zero_ct)

pclas = [i.get("Pclass") for i in li]

new_dic = {i:pclas.count(i) for i in pclas}

# print(new_dic)

yougest_oldest = [i.get("Age") for i in li]

min_age = min(yougest_oldest)

max_age = max(yougest_oldest)

# print(min_age)

# print(max_age)




first_ten_age = li[:10]

result = [i.get("Name") for i in first_ten_age]

# print(result)


# passengers s,q,k count :

boarding_pass = [p.get("Embarked") for p in li if len(p.get("Embarked"))>0]

# print(boarding_pass)

bc = {c:boarding_pass.count(c) for c in boarding_pass}

# print(bc)


all_pass=[i for i in li if  i.get("Age").isdigit()  and int(i.get("Age"))<10 ]


# print(len(all_pass))

survived_children = [p for p in all_pass if p.get("Survived")=="1"]

# print(len(survived_children))


total_pass = len(li)

# print(total_pass)


# total_no of males

total_males = [i for i in li if i.get("Sex")=="male"]

total_male_count = len(total_males)


total_females= [f for f in li if f.get("Sex") =="female"]

total_female_count = len(total_females)


survived_male = [i for i in li if i.get("Survived")=="1"]

survived_rate_m = (len(survived_male)/total_male_count)*100

# print(survived_rate_m)

survived_female = [ f for f in li if f.get("Survived")=="1"]

sur_female_rate = (len(survived_female)/total_female_count)*100

# print(sur_female_rate)



# survived_c = {z:li.count(z) for z in li if z.get("Survived")=="1"}

# print(survived_c)

total_pclass = [i.get("Pclass")  for i in li  ]

tc= {c:total_pclass.count(c) for c in total_pclass }

# print(tc)



c = [i.get("Pclass") for i in li if i.get("Survived")=="1"]

ct = {i:c.count(i) for i in c}

# print(ct)




