def is_anagram_count(word1,word2):

    is_anagram_count=True

    if len(word1)!=len(word2):

        return False
    
    for ch in word1:

        count_in_word1 = word1.count(ch)

        count_in_word2 = word2.count(ch)

        if count_in_word1 !=count_in_word2:

            is_anagram_count = False

            break

    return is_anagram_count
    
print(is_anagram_count("cat","acts"))

