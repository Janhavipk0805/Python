# Q4. Employee Salary Calculator

# Function with default argument
def calculate_salary(basic_salary, bonus=2000):
    return basic_salary + bonus


# Basic salaries
emp1 = 100000
emp2 = 80000
emp3 = 150000


# Employee 1 - Default Argument
print(f"Employee 1 has basic salary {emp1} and total salary is {calculate_salary(emp1)}")


# Employee 2 - Positional Argument
print(f"Employee 2 has basic salary {emp2} and total salary is {calculate_salary(emp2, 2000)}")


# Employee 3 - Keyword Argument
print(f"Employee 3 has basic salary {emp3} and total salary is {calculate_salary(basic_salary=emp3, bonus=2000)}")