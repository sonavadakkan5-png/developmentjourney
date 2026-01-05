file_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\development-journey\\python-works\\file_handling\\perfect_num.txt"

fr = open(file_path,"r")

perfect_numbers = []


for line in fr:

    num = int(line.strip("\n"))

    sum =0

    for i in range(1,num):

        if num%i==0:

            sum+=i

    if sum ==num:

        perfect_numbers.append(num)


print(perfect_numbers)


    