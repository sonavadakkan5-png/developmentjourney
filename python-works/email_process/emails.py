email_path ="email_process\\email.txt"

gmail_path = "email_process\\gmail.txt"

yahoo_path = "email_process\\yahoo.txt"

outlook_path = "email_process\\outlook.txt"

fr=open(email_path,"r")

gmail_w=open(gmail_path,"w")

yahoo_w = open(yahoo_path,"w")

outlook_w = open(outlook_path,"w")

for line in fr:

    email_line = line.rstrip("\n")

    if email_line.endswith("@gmail.com"):

        gmail_w.write(email_line+"\n")

    elif email_line.endswith("@yahoo.com"):

        yahoo_w.write(email_line+"\n")

    elif email_line.endswith("@outlook.com"):

        outlook_w.write(email_line+"\n")

print("end program")




