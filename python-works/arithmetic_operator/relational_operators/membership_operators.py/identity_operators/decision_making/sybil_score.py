sybil_score = int(input("enter the sybil score:"))

if sybil_score in range(300,550):

    print("POOR")

elif sybil_score in range(550,650):

    print("AVERAGE")

elif sybil_score in range(650,750):

    print("GOOD")

elif sybil_score in range(750,901):

    print("EXCELENT")

else:

    print("invalid range:")

