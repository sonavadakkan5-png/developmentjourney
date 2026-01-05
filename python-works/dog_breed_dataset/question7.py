# List breeds whose longevity is more than 12 years.

import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def longevity_find (self):

        result = []

        for i in self.data:

            life_span = int(i["Longevity (yrs)"].split("-")[1])

            if life_span> 12:

                result.append(i["Breed"])

        print(result)

dog_instance = Dog()

dog_instance.longevity_find()