db_pin = 1234

db_balance = 50000

pin_num = int(input("enter the pin number:"))

if pin_num==db_pin:

    with_amount = int(input("enter the amount:"))

    if  with_amount <=db_balance:

        print("withdrawal successful")

    else:

        print("insufficent balance.")

else:

    print("incorrect pin")

