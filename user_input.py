class Student:
    def __init__(self,name,roll_no,age):
        self.name = name
        self.roll_no = roll_no
        self.age = age
    def display(self):
        print("Student Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Age:",self.age)


name =input("Enter your name:")
roll_no = int(input("Enter your roll no.:"))
age = int(input("Enter your age:"))
s1 = Student(name,roll_no,age)
print("\nStudent Details:")
s1.display()
     
