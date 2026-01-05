principal_amount=int(input("enter the amount:"))

interest_rate=int(input("enter the rate:"))

n=int(input("enter the n:"))  

r = interest_rate / (12 * 100) 

# [P×R×(1+R)^N] / [(1+R)^N−1]

emi_amount=(principal_amount*interest_rate*(1+interest_rate)**n)/((1+interest_rate)**n-1)

print(emi_amount)


