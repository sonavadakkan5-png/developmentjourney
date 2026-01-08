from json import load

file_path="json_works\\jobs.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr)

result = {i.get("title"):i.get("id") for i in data if i.get("id")==10}

print(result)

