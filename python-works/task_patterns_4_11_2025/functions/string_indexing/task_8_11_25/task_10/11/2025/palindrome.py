def is_palindrome(word):

    is_palin = True

    reverse = word[::-1]

    if reverse !=word:

        is_palin = False

    return is_palin

print(is_palindrome("malayalam"))