class Employee:
    def __init__(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    def display(self):
        print("Employee name:",self.name)
        print("Employee id:",self.id)
        print("Employee Salary:",self.salary)
e1 = Employee("Atharva",101,25000)
e1.display()