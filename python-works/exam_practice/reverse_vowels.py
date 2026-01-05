# Reverse only vowels in a string
# Input: "hello" → Output: "holle"

text = "helloworld"

vowels = "aeiouAEIOU"

extract_vowels = [ i  for i in text if i in vowels]

extract_vowels.reverse()#oe

result = ""

for i in text:

    if i in vowels:

        result+=extract_vowels.pop(0)

    else:

        result+=i

print(result)

