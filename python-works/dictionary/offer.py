product = {"code":12,"title":"T-shirt","price":500,"size":"small"}

if "offer" in product:

    product["offer"]+=50   #update

else:

    product["offer"]=100   #add

print(product)