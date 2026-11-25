try:
    print(x)
    print(str)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else happened.")