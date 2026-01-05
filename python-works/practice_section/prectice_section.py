# # # The Reverser:

# # # Take the string "Python is fun".

# # # Split it into words.

# # # Reverse the list of words.

# # # Join them back into a single string with a space. What is the final output?


# # string = "Python is fun"

# # words = string.split()

# # reverse = words[::-1]

# # result = " ".join(reverse)

# # print(result)



# # num = ["1","2","3","4","5"]

# # # z=reversed(num)

# # z= num[::-1]

# # cl = list(z)

# # j = "".join(cl)

# # r = j.replace(",","")

# # print(r)

# # string = "good morning"

# # sj = "".join(string)

# # sp = sj.replace(" ","")

# # print(sp)




# You have a string of comma-separated values: "Alice,Bob,Charlie,David".

# Use split() to create a list of names.

# Now, take that list and join it back together using a semicolon (;) as the delimiter. What does the new string look like?

string =" This is a string with irregular spaces "

sp = string.split()

li = list(sp)

j = "".join(li)

print(li)


