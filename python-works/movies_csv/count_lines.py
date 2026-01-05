file_path = "movies_csv\\movies.txt"

fr = open(file_path,"r")

count = 0

header = fr.readline()

for line in fr:

    line = line.strip()

    if line:

        count+=1

print(count)

