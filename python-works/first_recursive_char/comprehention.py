arr =[1,2,3,4,5,6]

squares = [ num**2 for num in arr]

print(squares)


cubes = tuple( num**3 for num in arr)#just mention the tuple()


print(cubes)



#condition :

even = [ num for num in arr  if num%2==0]

print(even)

odd = tuple(num for num in arr if num%2!=0)

print(odd)


num_gt_five=[num for num in arr if num>5]

print(num_gt_five)


words =["profession","cat","act","program","dam","process"]

new_list = {ch for ch in words if ch.startswith("pro")}

print(new_list)


new_list1 = {ch for ch in words if ch.endswith("am")}

print(new_list1)



