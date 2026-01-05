#  Flatten a nested list using comprehension.
# Sample Input: [[1,2], [3,4], [5,6]]
# Sample Output: [1,2,3,4,5,6]


nested= [[1,2], [3,4], [5,6]]

result =[ num for sublist in nested for num in sublist]  

print(result)