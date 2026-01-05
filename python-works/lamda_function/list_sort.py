person1 = [
    ["alpha",100000,8],
    ["beta",20000,7],
    ["omega",12000,2],
]

person1_sa = sorted(person1,key=lambda k: k[2])

print(person1_sa)