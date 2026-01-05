treasure ={

    "box1":"gold",

    "box2":"silver",

    "box3":"diamond",

    "box4":"platinum"
}


#add box5 - iron

treasure["box5"]="iron"

print(treasure)

# check if box 6 exist if not add box6 with value copper

if "box6" not in treasure:

    treasure["box6"]="copper"

print(treasure)


#iteration

for k in treasure:

    print(k,treasure[k])


for k in treasure:

    print(k)

for k in treasure.keys():

    print("keys=",k)


for v in treasure.values():

    print("values=",v)


for k,v in treasure.items():

    print(k,v)

# get() ->if the key is inavlid so return none replace none to another we add the text after the get()


print(treasure.get("box10","empty box"))


print("task1")

print("task2")


# pop() -> is used to remove a key value in the dict

treasure.pop("box3")

print(treasure)