# 1 A A A
# 1 1 A A
# 1 1 1 A
# 1 1 1 1

for i in range(1,5):

    for j in range(1,5):

        if i>=j:

            print("1",end=" ")

        else:

            print("A",end=" ")

    print()