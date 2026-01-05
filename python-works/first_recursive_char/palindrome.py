# words = ["cat","act","madam","malayalam","dam"]

# palidromic_word =[ w for w in words if w ==w[::-1]]

# print(palidromic_word)



# num = [10,20,30,40,50]

# squares = { n:n**2 for n in num }

# print(squares)



# arr =[4,5,6,7]

# pattern_sum = [ sum (arr) -num for num in arr ]

# print(pattern_sum)




word =["am","in","on","off","in","out","off"]

word_dict = {}

for ch in word:

    if ch not in word_dict:

        word_dict[ch]=1

    else:

        word_dict[ch]+=1

print(word_dict)   # another way


word =["am","in","on","off","in","out","off"]


wc={w:word.count(w)for w in word}

print(wc)


text ="pythonprogramming"


tc ={ i:text.count(i) for i in text}

print(tc)






