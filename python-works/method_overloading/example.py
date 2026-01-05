class Animal:

    def __init__(self,name):

        self.name= name


    def sound(self):

        print(self.name,"sound")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):

        print(self.name,"bow...bow") 


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def sound(self):

        print(self.name,"miyavooo.....")

cat_instance = Cat("veluu")

cat_instance.sound()

dog_instance = Dog("chimban")

dog_instance.sound()
