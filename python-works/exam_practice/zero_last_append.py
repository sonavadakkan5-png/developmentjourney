# Input: [0,1,0,3,12] → Output: [1,3,12,0,0]


text = [0,1,0,3,12]

list1=[]

list2=[]

for i in text:

    if i==0:

        list1.append(i)

    else:

        list2.append(i)


print(list2+list1)