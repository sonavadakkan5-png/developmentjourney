num = int(input("enter the number:"))  #123

count =0

while(num!=0):

    last_digit = num%10

    count = count+1

    num = num//10

print("count =",count)


