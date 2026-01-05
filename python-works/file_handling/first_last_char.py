file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\first_last_char.txt"

fr = open(file_path,"r")

ch = []

for line in fr:

    line = line.strip()

    first = line[0]

    last = line[-1]

    app = first+last

    ch.append(app)

print(ch)

