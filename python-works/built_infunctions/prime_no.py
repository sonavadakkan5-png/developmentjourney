number = 15

check = [ not any(number%i==0 for i in range(2,number))]

print(check)