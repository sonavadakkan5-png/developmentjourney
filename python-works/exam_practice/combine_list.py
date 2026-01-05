str1 = ["a","c","d","e"]

str2 = [1,2,3,4,5,6,7]

empty_str =""

for i in range(len(str1)):

    empty_str+=str1[i]+str(str2[i])
print(empty_str)