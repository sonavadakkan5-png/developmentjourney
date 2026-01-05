file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\last_digit.txt"

fr = open(file_path,"r")

last_digit =[]

for line in fr:
    num = int(line.strip())     
    last = num % 10             
    last_digit.append(last)

print(last_digit)