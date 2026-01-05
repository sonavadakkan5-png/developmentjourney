def is_prime(number):

    flag =True

    for i in range(1,number):

        if number%i==0:

            flag=False

            break

        return flag
    
print(is_prime(5))





