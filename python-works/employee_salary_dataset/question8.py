# print employee detauls who experience > 20

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def exp(self):

        experience = [i for i in self.data if i.get("Experience_Years")> "20"]

        print(experience)

isinstance = Employee()

isinstance.exp()

