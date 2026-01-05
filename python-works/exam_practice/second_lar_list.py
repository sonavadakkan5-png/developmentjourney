# nums = [10, 40, 25, 30, 40, 5]

# convert_set = set(nums)

# convert_list=list(convert_set)

# convert_list.sort()

# sec_larg = convert_list[-2]

# print(sec_larg)


nums = [10, -40, 25, -30, 40, 5]

empty_list =[]

largest =0

sec_largest =0

for i in nums:

    if i>largest:

        largest=i

for i in nums:

    if i !=largest:

        empty_list.append(i)

for i in empty_list:

    if i >sec_largest:

        sec_largest=i

print(sec_largest)
