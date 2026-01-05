class Rbi:

    def gold_loan(self):

        print("gold loan rate:",8.5)

    def home_loan(self):

        print("home loan rate",9.2)

    def car_loan(self):

        print("car loan",8.5)

class Hdfc(Rbi):

    def gold_loan(self):

        print("gold loan rate:",9.5)

    def home_loan(self):

        print("home loan rate",10)

    def car_loan(self):

        print("car loan",9.7)

isinstance = Hdfc()

isinstance.car_loan()

isinstance.gold_loan()

isinstance.home_loan()

