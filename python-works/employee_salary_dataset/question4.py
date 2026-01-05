# Count how many employees are Male and how many are Female.


import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def male_count(self):

        male_count_find = [i for i in self.data if i.get("Gender")=="Male"]

        print(len(male_count_find))

    def female_count(self):

        female_count_find = [i for i in self.data if i.get("Gender")=="Female"]

        print(len(female_count_find))

emp_instance = Employee()

emp_instance.male_count()

emp_instance.female_count()