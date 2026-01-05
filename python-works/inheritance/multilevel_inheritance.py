class Grandparent:

    def properties(self):

        print("50 sqt land")

class Parent(Grandparent):

    def vehicle(self):

        print("breeza")

class Child(Parent):

    def gadgets(self):

        print("iphone")

instance1 = Child()

instance1.gadgets()

instance1.vehicle()

instance1.properties()