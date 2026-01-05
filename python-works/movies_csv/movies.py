file_path = "movies_csv\\movies.txt"

fr = open(file_path,"r")

count =0

for line in fr:

    line = line.strip()

    print(line)

    count+=1

    if count==5:

        break



