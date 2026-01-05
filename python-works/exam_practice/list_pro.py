# [1,2,2,3,4,4,5] → [1,2,3,4,5]

list1 = [1,2,2,3,4,4,5] 

empty_list =[]

for i in list1:

    if i not in empty_list:

        empty_list.append(i)

print(empty_list)