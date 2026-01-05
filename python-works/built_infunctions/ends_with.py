lst = [ "housefull","beautiful","peaceful","harmful","thinkful","powerful"]

bool_list = [i.endswith("ful") for i in lst]

result = all(bool_list)

print(result)