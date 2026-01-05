class Calculator:

    def add(self,*args):

        print(sum(args))

instance1 = Calculator()

instance1.add(10,20)