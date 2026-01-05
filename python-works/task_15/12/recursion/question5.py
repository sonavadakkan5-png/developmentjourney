#  Write a recursive function to count the number of digits in a given number.

def digit(n):

    if n==0:

        return 0
    
    return 1 + digit(n//10)

print(digit(12347))