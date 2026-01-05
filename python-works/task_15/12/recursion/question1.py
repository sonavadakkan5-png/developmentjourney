#  Write a recursive function to print numbers from 1 to N.

def numbers(n):

    if n==0:

        return
    
    numbers(n-1)

    print(n)

numbers(10)







