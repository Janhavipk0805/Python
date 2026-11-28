class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        print("Roll No:",self.roll_no)
        print("Name:",self.name)
s1 = Student("Priya",101)
s2 = Student("Janhavi",102)
print("\nStudent1:")
s1.display()
print("\nStudent2:")
s2.display()