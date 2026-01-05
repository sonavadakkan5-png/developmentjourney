# How many dog breeds are present in the dataset
import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def all_record(self):

        all_records = [i for i in self.data]

        print(len(all_records))

dog_instance = Dog()

dog_instance.all_record()