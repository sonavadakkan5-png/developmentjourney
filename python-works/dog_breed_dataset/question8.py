
import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def list_brred (self):

        result = []

        for i in self.data:

            list_breedd = i["Character Traits"].split(",")[2]

            result.append(i["Breed"])

        print(result)

dog_instance = Dog()

dog_instance.list_brred()