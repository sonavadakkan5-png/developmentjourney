# Print the names of employees from Delhi.


import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_emp(self):

        all_emp_det = [ i.get("Name")for i in self.data if i.get("City")=="Delhi"]

        print(all_emp_det)

emp_instance = Employee()

emp_instance.all_emp()