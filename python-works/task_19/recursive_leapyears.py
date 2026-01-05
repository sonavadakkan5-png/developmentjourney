years = [2005,2004,2008,2010,2024,2028,2024,2005]

e_dict ={}

for y in years:

    if y%100==0 and y%400==0 or y%100!=0 and y%4==0:

        if y not in e_dict:

            e_dict[y]=1

        else:

            e_dict[y]+=1

for k,v in e_dict.items():

    if v>1:

        print(k)