# Find breeds that have both respiratory issues and eye problems.


import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def rep(self):

        find_rep = [i for i in self.data if i.get("Breed")=="Labrador Retriever"]

        print(find_rep)

dog_instance = Dog()

dog_instance.rep()