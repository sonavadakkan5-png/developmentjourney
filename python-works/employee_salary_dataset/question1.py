# Print the total number of employees.
import csv

class Employee:

    data = list

    def __init__(self):
        
        file_path = "employee_salary_dataset\\employee_salary_dataset.csv"

        fr = open(file_path,"r",encoding="utf-8")

        reader = csv.DictReader(fr)

        self.data = [i for i in reader]

    def total_number_emp(self):

        total_emp = [ i.get("Name")for i in self.data]

        print(len(total_emp))

emp_instance = Employee()

emp_instance.total_number_emp()

        