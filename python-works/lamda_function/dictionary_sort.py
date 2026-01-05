person_weight={

    "sona":50,

    "saniya":55,

    "priya":90,

    "janaki":25
}

srt = sorted(person_weight,key=lambda k: person_weight.get(k),reverse=True)

print(srt)


