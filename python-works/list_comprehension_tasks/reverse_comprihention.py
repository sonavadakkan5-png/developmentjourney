# Reverse each word in a list using comprehension.
# Sample Input: ['python', 'django', 'react']
# Sample Output: ['nohtyp', 'ognaid', 'tcaer']

text = ['python', 'django', 'react']

result =[i[::-1] for i in text]

print(result)

