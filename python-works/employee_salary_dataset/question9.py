# max_salary find 

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def max_salary(self):

        max_sal = [int(i.get("Monthly_Salary")) for i in self.data]

        max_find = max(max_sal)

        print(max_find)

emp_instance = Employee()

emp_instance.max_salary()

