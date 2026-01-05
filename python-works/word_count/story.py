story_path ="word_count\\story.txt"

f_s = open(story_path,"r")

dictt ={}

for line in f_s:

    line = line.strip("\n")

    words = line.split(" ")

    for w in words:

        w = w.rstrip(" ,")

        w = w.rstrip(" .")

        if w not in dictt:

            dictt[w]=1

        else:

            dictt[w]+=1

for k,v in dictt.items():

    if v>1:

        print(k,v)

print(dictt)


print("end program")

















