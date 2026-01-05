vehicles = [
    {"name": "Swift", "brand": "Maruti Suzuki", "price": 650000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Baleno", "brand": "Maruti Suzuki", "price": 820000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Creta", "brand": "Hyundai", "price": 1500000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "i20", "brand": "Hyundai", "price": 950000, "model": 2021, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Seltos", "brand": "Kia", "price": 1600000, "model": 2023, "color": "Silver", "fuel_type": "Diesel"},
    {"name": "Sonet", "brand": "Kia", "price": 1200000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Harrier", "brand": "Tata", "price": 1900000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "Nexon", "brand": "Tata", "price": 1200000, "model": 2022, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Punch", "brand": "Tata", "price": 800000, "model": 2023, "color": "Green", "fuel_type": "Petrol"},
    {"name": "XUV700", "brand": "Mahindra", "price": 2200000, "model": 2023, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Thar", "brand": "Mahindra", "price": 1700000, "model": 2022, "color": "Red", "fuel_type": "Petrol"},
    {"name": "Scorpio N", "brand": "Mahindra", "price": 2000000, "model": 2023, "color": "White", "fuel_type": "Diesel"},
    {"name": "City", "brand": "Honda", "price": 1500000, "model": 2021, "color": "Silver", "fuel_type": "Petrol"},
    {"name": "Amaze", "brand": "Honda", "price": 900000, "model": 2022, "color": "Grey", "fuel_type": "Petrol"},
    {"name": "Kiger", "brand": "Renault", "price": 800000, "model": 2021, "color": "Blue", "fuel_type": "Petrol"},
    {"name": "Duster", "brand": "Renault", "price": 1300000, "model": 2020, "color": "Brown", "fuel_type": "Diesel"},
    {"name": "EcoSport", "brand": "Ford", "price": 1100000, "model": 2021, "color": "White", "fuel_type": "Petrol"},
    {"name": "Endeavour", "brand": "Ford", "price": 3600000, "model": 2020, "color": "Black", "fuel_type": "Diesel"},
    {"name": "Altroz", "brand": "Tata", "price": 950000, "model": 2022, "color": "Golden", "fuel_type": "Petrol"},
    {"name": "Venue", "brand": "Hyundai", "price": 1300000, "model": 2023, "color": "Red", "fuel_type": "Petrol"}
]

for v in vehicles:

    if v.get("fuel_type")=="petrol":

        print(v.get("name"))









for v in vehicles:

    if v.get("color") =="Red":

        print(v.get("name"))

for v in vehicles:

    if v.get("model")==2022:

        print(v.get("name"))

for v in vehicles:

    if v.get("fuel_type")=="Diesel":

        print(v.get("name"))

result ={ v.get("price") for v in vehicles}

print(result)

for v in vehicles:

    if v.get("price") >1000000:

        print(v.get("name","price"))   

result =[v.get("name") for v in vehicles if v.get("price")>1000000]

print(result)




for v in vehicles:

    if v.get("brand")=="Tata":

        print(v.get("name"))


for v in vehicles:

    if v.get("brand")=="Maruti Suzuki":

        print(v.get("price"))
 

for v in vehicles:

    if v.get("brand")=="Hyundai" and v.get("price")>500000:

        print(v.get("name"))


for v in vehicles:

    if v.get("model")>=2022 and v.get("model")<=2024:

        print(v.get("name"))


empty_dict ={}

gretest=0

for v in vehicles:

    v["brand"]

    if v["brand"] not in empty_dict:

        empty_dict[v["brand"]]=1

    else:

        empty_dict[v["brand"]]+=1



for v in empty_dict.values():

    if v>gretest:

        gretest=v

for k,v in empty_dict.items():

    if gretest==v:

        print(k)


empty_dict ={}

largest =0

for v in vehicles:

    v["brand"]

    if v["brand"] not in empty_dict:

        empty_dict[v["brand"]]=1

    else:

        empty_dict[v["brand"]]+=1


for v in empty_dict.values():

    if v >largest:

        largest=v

for k,v in empty_dict.items():

    if v==largest:

        print(k)



empty_dict ={}

largest =0

for v in vehicles:

    v["model"]

    if v["model"] not in empty_dict:

        empty_dict[v["model"]]=1


    else:

        empty_dict[v["model"]]+=1

for v in empty_dict.values():

    if v > largest:

        largest=v

for k,v in empty_dict.items():

    if v == largest:

        print(k)






        