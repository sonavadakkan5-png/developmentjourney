# Get squares of odd numbers but store them as strings.
# Sample Input: [1,2,3,4,5]
# Sample Output: ['1','9','25']

input = [1,2,3,4,5]

result = [str(i**2) for i in input if i%2!=0]

print(result)