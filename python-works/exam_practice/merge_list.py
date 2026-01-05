list1 = [1, 2, 3,4,6]

list2 = [3, 4, 5]

merged = list1.copy()

for i in list2:

    if i not in merged:

        merged.append(i)

print(merged)

