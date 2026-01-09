from json import load

file_path="oscar_json\\oscar.json"

fr=open(file_path,"r",encoding="utf-8")

data = load(fr)

result = {i.get("name") for i in data}

print(result)

