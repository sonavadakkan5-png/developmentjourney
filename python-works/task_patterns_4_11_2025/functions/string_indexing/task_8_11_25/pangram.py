def pangram(text):

    # text = text.casefold()

    is_pangram = True

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for ch in alphabet:

        if ch not in text.casefold():

            is_pangram = False

            break

    return is_pangram

print(pangram("the quick brown fox jumps over lazy dog"))





