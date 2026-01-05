file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\words.txt"

fr = open(file_path,"r")

result = []

for line in fr:

    line = line.rstrip("\n")

    space_remove = line.replace(" ","")

    result.append(space_remove)

print(result)