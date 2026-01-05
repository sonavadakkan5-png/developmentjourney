#  Create a dictionary of character frequencies using comprehension.
# Sample Input: "banana"
# Sample Output: {'b':1, 'a':3, 'n':2}

str12 ="banana"

result ={i: str12.count(i) for i in str12}

print(result)
