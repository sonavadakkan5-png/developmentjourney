num1 = int(input("enter number1:"))

num2 = int(input("enter number2:"))

i=1

small = 0

if num1 < num2:

    small = num1

else:

    small = num2

while(i<=small):

    if(num1%i==0) and (num2%i==0):

        print(i)

    i+=1

