numbers = [2,4,5,10,13,14,13,11,7,9,7]

e_dic = {}

for num in numbers:

    is_prime = True

    for i in range(2,num):

        if num%i==0:

            is_prime = False

            break

    if is_prime == True:

        if num not in e_dic:

            e_dic[num]=1

        else:

            e_dic[num]+=1

for k,v in e_dic.items():

    if v>1:

        print(k)



