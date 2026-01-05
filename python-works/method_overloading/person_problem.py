class Person:

    name : str

    age : int

    gender : str 

    def __init__(self,name,age,gender):

        self.name = name 

        self.age = age

        self.gender = gender 

    @property    # decorate is a function that contain one feature 

    def get_age(self):

        print(self.age)

    @property

    def get_gender(self):

        print(self.gender)


instance_1 = Person("sona",22,"female")

instance_1.get_age

instance_1.get_gender