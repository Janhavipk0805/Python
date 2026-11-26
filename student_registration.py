student_id = "Janhavi"
try:
    print(int(student_id))
except ValueError as e:
    print("Invalid Student ID:",e)
print("Registration Process completed")