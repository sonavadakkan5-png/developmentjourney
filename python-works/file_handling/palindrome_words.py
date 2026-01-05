file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\words.txt"

fr = open(file_path,"r")

result = []

for line in fr:

    line = line.rstrip("\n")

    space_remove = line.replace(" ","")

    rev = space_remove[::-1]

    if rev ==space_remove:

        result.append(rev)

print(result)