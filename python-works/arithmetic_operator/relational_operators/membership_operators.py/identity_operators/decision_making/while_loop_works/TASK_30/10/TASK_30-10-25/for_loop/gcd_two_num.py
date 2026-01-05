num1 = int(input("enter number1:"))   #6

num2 = int(input("enter number2:"))   #12

small = min(num1,num2)  #min(6,12)=6

gcd = 0  #gcd=0

for i in range(1,small+1):   #range(1,6+1)=(1,7)

    if num1%i==0 and num2%i==0: 

        gcd =i

print(gcd)



