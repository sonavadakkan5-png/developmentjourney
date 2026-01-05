from abc import ABC

from abc import abstractmethod

class Film(ABC):

    @abstractmethod

    def malayalam(self):

        pass

    def tamil(self):

        pass

    def hindi(self):

        pass

class Actors(ABC):

    def malayalam(self):

        print("mohalal")

    def tamil(self):

        print("surya")

    def hindi(self):

        print("aditya roy kapoor")

instance = Actors()

instance.hindi()

instance.malayalam()

instance.tamil()



     
