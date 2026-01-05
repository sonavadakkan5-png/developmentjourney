def vowel_count(word):

    count =0

    vowels="aeiou"

    for ch in word.casefold():

        if ch  not in vowels and ch.isalpha():

            count+=1


    return count

print(vowel_count("hello"))
print(vowel_count("hello123"))





