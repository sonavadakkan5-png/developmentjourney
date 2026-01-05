file_path = "movies_csv\\movies.txt"

fr = open(file_path,"r")

header = fr.readline().strip()

column = header.split(" ,")

for i in column:

    print(i)

    