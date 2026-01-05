# Extract words longer than 5 characters from a sentence.
# Sample Input: "Python programming is very interesting"
# Sample Output: ['Python', 'programming', 'interesting']

words =['Pyth', 'programming', 'interesting',"sona"]

list_compre =[i for i in words if len(i)>5]

print(list_compre)