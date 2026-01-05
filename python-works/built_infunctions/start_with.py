words = ["program","problem","perfect","apple"]

bool_val = [i.startswith("pro") for i in words]

result = any(bool_val)

print(result)