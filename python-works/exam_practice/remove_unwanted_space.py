text = ["hai","hello"," ","None"," "]

em_lis = []

for i in text:

    if i.strip() and i != "None":

        em_lis.append(i)

print(em_lis)
