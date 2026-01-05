num1 = int(input("enter num1:"))

num2 = int(input("enter num2:"))

num3 = int(input("enter num3:"))

smallest = min(num1,num2,num3)

for i in range(1,smallest+1):

    if num1%i==0 and num2%i==0 and num3%i==0:

        print(i) 