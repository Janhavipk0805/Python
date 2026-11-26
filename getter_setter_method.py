class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        self.__marks=marks
s = Student()
print("Before setter methods are:",s.get_marks())
s.set_marks(95)
print("After modification marks are:",s.get_marks())
