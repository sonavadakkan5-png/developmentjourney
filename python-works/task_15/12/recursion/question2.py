# Write a recursive function to find the sum of first N natural numbers

def find_sum(n):

    if n==1:

        return 1
    
    return n+find_sum(n-1)

print(find_sum(10))

