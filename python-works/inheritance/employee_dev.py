class Employee:

    id : int

    department : str

    salary : int

    def __init__(self,id,department,salary):

        self.id = id

        self.department = department

        self.salary =salary

    def display(self):

        print(f"id={self.id}department={self.department}salary={self.salary}")


class Developer(Employee):

    programming_language : str

    framework : str

    def __init__(self, id, department, salary,programming_language,framework):

        super().__init__(id, department, salary)

        self.programming_language=programming_language

        self.framework=framework

    def display(self):

        super().display()

        print(self.programming_language,self.framework)

instance = Developer(12,"ff",12345,"java","ghj")

instance.display()

            

        