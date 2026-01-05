class Person:

    name : str

    age : int

    gender : str 


    def __init__(self,name,age,gender):

        self.name = name

        self.age = age

        self.gender =gender

    def display(self):

        print(f"name={self.name} age={self.age} gender={self.gender}")

class Student(Person):

    roll_no :int

    course : str

    def __init__(self,name,age,gender,roll_no,course):

        super().__init__(name,age,gender)

        self.roll_no=roll_no

        self.course =course

    def display(self):

        super().display()

        print(f" rollno={self.roll_no} course={self.course}")

student_instance = Student("sona",22,"female",12,"mca")

student_instance.display()





