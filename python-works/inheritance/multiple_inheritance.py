class Father:

    def father_skill(self):

        print("cricket")

class Mother:

    def mother_skill(self):

        print("cooking")

class Child(Father,Mother):

    def skill(self):

        print("skill")

instance1= Child()

instance1.father_skill()

instance1.mother_skill()

instance1.skill()



