file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\greetings.txt"

fr = open(file_path,"r")

st = set()

for line in fr:

    st.add(line.rstrip("\n"))

print(st)