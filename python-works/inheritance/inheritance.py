# inheritance 

class Parent:

    def vehicle(self):

        print("this is a vehicle breeza")

class Child(Parent):

    def mobile(self):

        print("this is a mobile vivo")

child_instance = Child()

child_instance.mobile()

child_instance.vehicle()