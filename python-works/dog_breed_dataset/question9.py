# Find breeds that are energetic and intelligent.

import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def both_find(self):

        result = []

        for i in self.data:

            Character_Traits = i["Character Traits"].lower()

            if "energetic" in Character_Traits and "intelligent" in Character_Traits:

                result.append(i["Breed"])

        print(result)

dog_instance = Dog()

dog_instance.both_find()