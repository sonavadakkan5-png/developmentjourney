word = "abcdcdeffgffasffff"

check = "ab"

count = 0

for i in range(0,14):

    sli = word[i:i+2]

    if check == sli:

            count+=1

print(count)



