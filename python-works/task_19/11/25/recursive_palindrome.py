words = ["cat","act","madam","hello","madam"]

e_dict ={}

for w in words:

    if w ==w[::-1]:

        if w not in e_dict:

            e_dict[w]=1

        else:

            e_dict[w]+=1

for k,v in e_dict.items():

    if v>1:

        print(k)

