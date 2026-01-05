# List all unique countries of origin.

import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def all_unique(self):

        all_unique_countries = [  i.get("Country of Origin")for i in self.data]

        print(set(all_unique_countries))

dog_instance = Dog()

dog_instance.all_unique()