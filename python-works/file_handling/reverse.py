file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\num.txt"

fr = open(file_path,"r")

result = []

for line in fr:

    line = line.rstrip("\n")

    rev = line[::-1]

    result.append(rev)

print(result)