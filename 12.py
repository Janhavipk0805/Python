try:
    num = int(input("Enter a number:"))
    result = 50/num
except ZeroDivisionError as e:
    print("Exception:",e)