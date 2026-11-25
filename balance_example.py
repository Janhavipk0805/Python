balance = 10000
try:
    amount = float(input("Enter withdrawal amount:"))
    if amount < 0:
       raise Exception("Value is positive")
    if amount > balance:
        raise Exception("Transaction failed !")
    balance -= amount
    print("Withdrawal Successful !")
    print("Remaining balance:",balance)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
     