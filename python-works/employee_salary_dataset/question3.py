# Print all employees who work in the IT department.

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_emp(self):

        all_emloyee = [i for i in self.data if i.get("Department")=="IT"]

        print(all_emloyee)

emp_instance = Employee()

emp_instance.all_emp()