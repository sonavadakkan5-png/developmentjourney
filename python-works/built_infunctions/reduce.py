from functools import reduce

lst = [1,5,8,1,4,7]

max_num = reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)

print(max_num)

min_num = reduce(lambda n1,n2: n1 if n1<n2 else n2,lst)

print(min_num)

p_num = reduce(lambda n1,n2:  n1*n2 ,lst)

print(p_num)

