class Bank:

    acc_num : int

    name : str

    acc_type : str
    
    balance : int

    def create_account(self,acc_num,name,acc_type,balance):

        self.acc_num = acc_num

        self.name = name

        self.acc_type = acc_type

        self.balance = balance

    def deposite(self,amount):

        self.balance +=amount

        print(f"your account{self.acc_num} created with {amount} your available balance is {self.balance}")

    def withdraw(self,amount):

        if amount<self.balance:

            self.balance -=amount

            print(f"your account{self.acc_num} created with {amount} your available balance is {self.balance}")

        else:

            print("transaction failed insufficent balance")

    def display(self):

        print(self.acc_num,self.name,self.acc_type,self.balance)

isinstance1 = Bank()

isinstance1.create_account(1,"canara","c",1000)

isinstance1.deposite(1000)

isinstance1.withdraw(200)

isinstance1.display()




         

