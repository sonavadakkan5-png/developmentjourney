set1 = {10,20,30,20,20}

set2= {20,30,20,40,50,10}

set_union = set1.union(set2)

print(set_union)

set_intersection = set1.intersection(set2)

print(set_intersection)

set_difference = set2.difference(set1)

print(set_difference)

# superset: if set b is a superset of set a set b contain all elements in a 


print(set1.issuperset(set2))

