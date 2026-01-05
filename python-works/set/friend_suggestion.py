all_users = {"sachin","dravid","laxmn","ganguly","sreenath","zaheer","dhoni","yuvi","kaif"}

sachin_frds = {"dravid","laxman","ganguly"}

dhoni_fr = {"dravid","laxman","yuvi","kaif"}

diff = all_users.difference(sachin_frds)

print(diff)

diff.remove("sachin")

print(diff)

inter = sachin_frds.intersection(dhoni_fr)

print(inter)


symmetric_diff=all_users.symmetric_difference(sachin_frds)

print(symmetric_diff)




num = {10,20,30,10}

num2 = {10,20,50,70,80}

sd = num.symmetric_difference(num2)

print(sd)