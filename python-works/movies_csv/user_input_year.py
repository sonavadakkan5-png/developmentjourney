file_path = "movies_csv\\movies.txt"

user_inp = input("enter the year:").strip()

fr = open(file_path,"r")

header = fr.readline()

for line in fr:

    line = line.strip()

    if line:

        columns = line.split("\t")

        year = columns[-1].strip()

        if year == user_inp:

            print(columns[0])

