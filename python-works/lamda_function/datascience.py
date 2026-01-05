sttendance=[

    {"name":"abin","attendance_count":28,"count":1},
    {"name":"aadhil","attendance_count":20,"count":2},
    {"name":"adhnan","attendance_count":20,"count":2},
    {"name":"arya","attendance_count":25,"count":5},
    {"name":"clairin","attendance_count":25,"count":4},
    {"name":"joji","attendance_count":26,"count":7},
    {"name":"libin","attendance_count":28,"count":7},
    {"name":"lijo","attendance_count":21,"count":2},
    {"name":"shajeer","attendance_count":27,"count":2},
    {"name":"shafi","attendance_count":28,"count":7},
    {"name":"resin","attendance_count":24,"count":3},
    {"name":"lakshmi","attendance_count":16,"count":6},
    {"name":"thammana","attendance_count":25,"count":1},
    {"name":"VARSHANA","attendance_count":8,"count":0},

]

c_sort = sorted(sttendance,key=lambda dic:dic.get("count"),reverse=True)

name_att = [{i.get("name"):i.get("count")} for i in c_sort]

# print(name_att)



c_max= max(sttendance,key=lambda dic:dic.get("count"))

# nam = [{i.get("name"):i.get("count")} for i in c_max]

print(c_max)

atte_count = sorted(sttendance,key=lambda k:k.get("attendance_count"))




