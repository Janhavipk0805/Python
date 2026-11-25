try:
    num = int(input("Enter a number:"))
    try:
        result = 10/num
        print(result)
    except ZeroDivisionError as e:
        print(e)
except ValueError as e:
    print(e)