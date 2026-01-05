class Course:

    course_name : str

    def __init__(self,course_name):

        self.course_name=course_name
    
    def display(self):

        print(self.course_name)

class Module(Course):

    module_name : str

    def __init__(self,course_name,module_name):

        super().__init__(course_name)

        self.module_name=module_name

    def display(self):

        super().display()

        print(self.module_name)

class Lesson(Module):

    lesson_name :str

    def __init__(self, course_name, module_name,lession_name):

        super().__init__(course_name, module_name)

        self.lesson_name=lession_name

    def display(self):

        super().display()

        print(self.lesson_name)

constructor = Lesson("python","django","constuu")

constructor.display()

