# Create a list of squares for only even numbers from a given list.
# Sample Input: [1, 2, 3, 4, 5, 6]
# Sample Output: [4, 16, 36]

list_squres =[1, 2, 3, 4, 5, 6]

list_com = [i**2 for i in list_squres if i%2==0]

print(list_com)
