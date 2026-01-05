class Framework:

    name : str

    language :str

    architecture : str

    def set_framework(self,name,language,architecture):

        self.name = name

        self.language = language

        self.architecture = architecture

    def display(self):

        print(self.name,self.language,self.architecture)

framwork_instance1 = Framework()

django = framwork_instance1.set_framework("python","asp","mvt")

framwork_instance1.display()

