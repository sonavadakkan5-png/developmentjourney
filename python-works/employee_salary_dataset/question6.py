# Print employees whose Age is above 50.

import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def all_age(self):

        age= [i for i in self.data if int( i.get("Age"))>50]

        print(age)

emp_instance = Employee()

emp_instance.all_age()