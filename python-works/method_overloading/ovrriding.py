class Vehicle:

    def __init__(self,brand,title):

        self.brand = brand

        self.title = title

    def move(self):

        print(self.title,"is moving")


class Car(Vehicle):

    def __init__(self, brand, title):
        super().__init__(brand, title)

class Ship(Vehicle):

    def __init__(self, brand, title):
        super().__init__(brand, title)

    def move(self):

        print(self.title,"is sailing")

car_instance = Car("maruthi","breeza")

ship_instance = Ship("caribian","titanic")

car_instance.move()

ship_instance.move()

