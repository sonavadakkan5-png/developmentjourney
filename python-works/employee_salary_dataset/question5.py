# Find the maximum salary in the dataset.

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def find_min_salary(self):

        ma_salary = [int(i.get("Monthly_Salary")) for i in self.data]

        print( min(ma_salary))

emp_instance = Employee()

emp_instance.find_min_salary()
