# #Program 1: Program handling zero exception
# try:
#      a = 10
#      b = 0
#      result = a/b
#      print(result)
# except ZeroDivisionError as e:
#        print(e)
# print("Program completed")


# print("Program started...")
# print("Just a sec...")
# try:
#     num = int(input("Enter a number:"))
#     result = 100/num
#     print("Result:",result)
# except ValueError:
#     print("Invalid input")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("Program executed successfully!")
# finally:
#     print("This is the mandatory block.")
# try:
#     age = 10
#     if age < 18:
#         raise ValueError("Legally mature")
# except ValueError as e:
#     print(e)
# else:
#     print("Access granted")


# A custom exception in Exception class
# Syntax:
# class MyCustomException(Exception):
#     pass
# where , 
# class defines  a new class.
# MyCustomException is the exception's name.
# Exception is the parent class .

class MyCustomException(Exception):
    pass
try:
    age = 16
    if age < 18:
        raise ValueError("Age must be above 18")
# except ValueError as e:
#     print(e)
#else:
   # print("Access granted")
finally:
    print("Program end.")