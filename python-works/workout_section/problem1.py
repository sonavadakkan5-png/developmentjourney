# def newprogram(word):

#     count =1

#     string =""

#     for i in range(1,len(word)):

#         if word[i]==word[i-1]:

#             count+=1

#         else:

#             string+=str(count)+word[i-1]

#             count =1 

#     string+=str(count) + word[-1]

#     return string

# print(newprogram("aaabbc"))


# w = " hello world"

# split_w = w.split()

# list1 = []

# for i in split_w:

#     list1.append(i[::-1])

# print(" ".join(list1)) 

# words = ["I", "am", "learning", "Python"]

# new = []

# for i in words:

#     new.append(i)

# x= " ".join(new)

# print(x)

# nums = [10, 20, 30, 40]

# list1 = []

# for i in nums:

#     list1.append(i)

# x=",".join(map(str,list1))

# print(x)

# s = "hello world python"

# y=s.split()

# list1 = []

# for i in y:

#     list1.append(i[::-1])

# x = " ".join(list1)

# print(x)





word = "hello world program"

x=word.split(" ")

list1= []

for i in x:

    list1.append(i[::-1])

    y=" ".join(list1)

print(y)












