file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\num.txt"

fr = open(file_path,"r")

odd_num = []

even_num = []

for line in fr:

    ev = int(line.rstrip("\n"))

    if ev %2==0:

        even_num.append(ev)

    else:

        odd_num.append(ev)

print(odd_num)

print(even_num)