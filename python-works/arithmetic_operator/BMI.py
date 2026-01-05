weight_in_kg = int(input("enter your weight in kg:"))

height_in_cm = int(input("enter your height in cm:"))

height_in_meter = height_in_cm/100

bmi=weight_in_kg/(height_in_meter**2)

print(round(bmi,3))



