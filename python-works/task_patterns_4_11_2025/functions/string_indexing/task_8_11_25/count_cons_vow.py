def display_vowel_and_consonant_count(word):

    v_count =0

    c_count=0

    vowels="aeiou"

    for ch in word.casefold():

        if ch in vowels:

            v_count+=1

        elif ch.isalpha():

            c_count+=1

    print(v_count)

    print(c_count)


display_vowel_and_consonant_count("hello123")



