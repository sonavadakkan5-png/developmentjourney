# error handling : 

num1 = int(input("enter number 1:"))

num2 = int(input("enter number 2:"))

try:

    divide = num1/num2

    print(divide)

except Exception as e :

    print(e)

print("end program:")