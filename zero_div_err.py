try:
    a = 10
    b = 0
    print(a/b)
except NameError:
    print("Variable b is not defined")
except:
    print("Something else went wrong")