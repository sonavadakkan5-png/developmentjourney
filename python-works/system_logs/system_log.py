system_path = "system_logs\\system_log.txt"

warning_path = "system_logs\\warning.txt"


error_path = "system_logs\\error.txt"


info_path = "system_logs\\info.txt"

fr=open(system_path,"r")

Warning_w=open(warning_path,"w")

error_w = open(error_path,"w")

info_w = open(info_path,"w")

for line in fr:

    system_line = line.rstrip("\n")

    x=system_line.split(" ")[2].casefold()

    if x=="error":

        error_w.write(line+"\n")

    elif x=="warning":

        Warning_w.write(line+"\n")

    elif x=="info":

        info_w.write(line+"\n")

print("end program")



    

        



 