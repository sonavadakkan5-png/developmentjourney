words = ["hello","hai","hello","is"]

recursive = []

not_recursive = []

for w in words:

    count = words.count(w)

    if count >1 and w not in recursive:

        recursive.append(w)

    elif count==1 and w not in not_recursive:

        not_recursive.append(w)

print(recursive)

print(not_recursive)


