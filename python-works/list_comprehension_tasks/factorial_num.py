# Generate a dictionary of number: factorial for numbers 1–10.
# Sample Output: {1:1, 2:2, 3:6, ..., 10:3628800}

empty_dict ={}

fact = 1

for i in range(1,11):

    fact=fact*i

    empty_dict[i]=fact

print(empty_dict)



