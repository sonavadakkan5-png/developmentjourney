num1 = int(input("enter number1:"))

num2 = int(input("enter number2:"))

num3 =int(input("enter number3:"))

i=1

small =0

if (num1<num2) and (num2<num3):

    small = num1

elif (num2<num3) and (num2<num1):

    small = num2

else:

    small=num3

while(i<=small):

    if(num1%i==0) and (num2%i==0) and (num3%i==0) :

        print(i)

    i+=1

    




