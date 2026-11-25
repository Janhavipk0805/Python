try:
    print("Processing Transaction...")
    amount = int(input())
    if amount > 10000:
        print("Transaction successfull")
    else:
      print("Transaction failed !!! ")
except:
    print("Invalid input")
finally:
    print("Thank You !")