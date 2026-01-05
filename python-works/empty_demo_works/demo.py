# text = "helloo"

# e_dic ={}

# for i in text:

#     if i not in e_dic:

#         e_dic[i]=1

#     else:

#         e_dic[i]+=1

#         print(i)

#         break


def first_rec(text):

    e_dict ={}

    for i in text:

        if i not in e_dict:

            e_dict[i]=1

        else:

            e_dict[i]+=1

            return i
        
print(first_rec("heloo"))