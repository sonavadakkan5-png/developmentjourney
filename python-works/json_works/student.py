from json import load

file_path = "json_works\\students.json"

fr = open(file_path,"r",encoding="utf-8")

data = load(fr) # convert json => to python native that means 

result = [ i.get("name") for i in data if i.get("course")=="python"]

print(result)