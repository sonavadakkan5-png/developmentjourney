class Phone:

    def __init__(self,title,price,brand,features):

        self.title = title

        self.price = price

        self. brand = brand

        self.features = features

    def display(self):

        print(self.title,self.price,self.brand,self.features)

phone_instance1 = Phone("oppo",100000,"gg","fgg")

phone_instance1.display()

phone_instance2 = Phone("oppo",100000,"gg","fgg")

phone_instance2.display()