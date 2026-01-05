file_path = "error_handling\\abc.py"

try:

    fr = (file_path,"r")

    for line in fr:

        print(line)

except Exception as e:

    print(e)

print("end program")