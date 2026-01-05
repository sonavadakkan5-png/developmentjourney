def count_vowels(s):

    count = 0

    vowels = "aeiou"

    for ch in s:

        if ch in vowels:

            count+=1

    return count
 
print(count_vowels("sonasunny"))
    


