arr = [1,5,7,9,12,15,16,19,20]

count_even = 0

count_odd = 0

for a in arr:

    if a%2==0:

        print(a,"is even")

        count_even+=1

    else:

        print(a,"is odd")

        count_odd+=1

print("even count is=",count_even)

print("odd count is=",count_odd)

