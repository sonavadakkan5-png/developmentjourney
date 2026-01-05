# dept unique print

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def unique(self):

        unique = [i.get("Department") for i in self.data]

        print(set(unique))

emp_instance = Employee()

emp_instance.unique()