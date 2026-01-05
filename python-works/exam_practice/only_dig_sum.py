# text = "pYtH0n23#2!455"

# dictt ={}

# for i in text:

#     if i.isdigit():

#         pass

#     elif i.isalpha():

#         pass

#     else:

#         dictt[i]=1


# print(dictt)


# another way 

text = "pYtH0n23#2!455"

dictt ={}

for i in text:

    if  not i.isalnum():

        dictt[i]=1

print(dictt)