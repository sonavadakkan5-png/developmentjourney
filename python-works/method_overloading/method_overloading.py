class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1,num2+num3)

    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

instance = Calculator()

instance.add(1,2,3,4)

# instance.add(1,2) get error 

