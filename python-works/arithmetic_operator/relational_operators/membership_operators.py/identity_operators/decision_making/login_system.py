password = 55555

otp = 123

ask_pass = int(input("enter the password:"))

if password == ask_pass:

    ask_otp =int(input("enter the otp:"))

    if otp == ask_otp:
        
        print("login successfull")

    else:

        print("incorrect otp")
else:

    print("incorrect password")

