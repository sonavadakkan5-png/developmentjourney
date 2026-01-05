file = open("numbers.txt","r")

even_num = []

odd_num =[]

for i in file:

    num = int(i.strip())


    if num%2==0:

        even_num.append(num)

    else:

        odd_num.append(num)


file.close()

print(even_num)

print(odd_num)

