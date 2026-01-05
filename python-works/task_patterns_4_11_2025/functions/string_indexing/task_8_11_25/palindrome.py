# word = "malayalam"

# reverse = word[::-1]

# print("palindrome")



#using function


def palindrome_word(word):

    word = word.casefold()

    return word ==word[::-1]

print(palindrome_word("malayalaM"))








