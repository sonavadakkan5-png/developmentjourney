from abc import ABC

from abc import abstractmethod

class Editor(ABC):

    @abstractmethod

    def create_module_pack(self):

        pass
    
    @abstractmethod
    def edit(self):

        pass
    @abstractmethod
    def execute(self):

        pass
    @abstractmethod
    def debugg(self):

        pass

class Vscode(Editor):

    def create_module_pack(self):
        
        print("vs code creating package and module")

    def edit(self):
        
        print("vs code edit")

    def execute(self):

        print("vs code execute")

    def debugg(self):
        
        print("cs code debugg")
    @property
    def new_method(self):

        print("new")

isinstance = Vscode()

isinstance.create_module_pack()

isinstance.debugg()

isinstance.edit()

isinstance.execute()

isinstance.new_method

