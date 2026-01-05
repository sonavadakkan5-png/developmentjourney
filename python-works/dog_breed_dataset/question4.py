# Find all breeds with Brown eye color


import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def brown_eye(self):

        find_brown_eye = [i for i in self.data if i.get("Color of Eyes")=="Brown"]

        print(find_brown_eye)

        print(len(find_brown_eye))

dog_instance = Dog()

dog_instance.brown_eye()