from copy import deepcopy

sona_fvt_food = [ 
    [" tea","banana fry"],

    ["rice","payasam"],

    [ "biriyani","aluporotta"],
]

sana_fvt_food =deepcopy(sona_fvt_food)

sona_fvt_food[1][1]="rasavada"

print(sana_fvt_food)

print(sona_fvt_food)

