# Count how many breeds originated from Germany

import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def all_breed(self):

        how_many_breed = [i for i in self.data if i.get("Country of Origin")=="Germany"]

        print(len(how_many_breed))

dog_instance = Dog()

dog_instance.all_breed()