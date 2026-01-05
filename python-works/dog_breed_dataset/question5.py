# List breeds that have Common Health Problems


import csv 

class Dog:

    data : list

    def __init__(self):
        
        file_path = "dog_breed_dataset\\dog_breeds.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i  in reader]

    def Common_Health_Problems(self):

        Common_health_pro = [i.get("Common Health Problems") for i in self.data]

        print(Common_health_pro)

dog_instance = Dog()

dog_instance.Common_Health_Problems()