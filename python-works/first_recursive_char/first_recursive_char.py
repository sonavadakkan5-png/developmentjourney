def first_recursive_char(word):

    wc ={}

    for i in word:

        if i in wc:

            return i
        
        else:

            wc[i]=1

    return None
    
print(first_recursive_char("ballon"))