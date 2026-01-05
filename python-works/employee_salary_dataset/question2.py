# Print the first 5 employee names,salary.

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def first_five_emp(self):

        first_five_employee = [(i.get("Name"),int(i.get("Monthly_Salary") )) for i in self.data[:5] ]

        print(first_five_employee)

emp_instance = Employee()

emp_instance.first_five_emp()

