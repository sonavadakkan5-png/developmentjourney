lst = [ 10,20,60,45,13,77]

even_list = [i%2==0 for i in lst]

result = all(even_list)

print(result)

