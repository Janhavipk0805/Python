balance = 10000
withdrawal = 5000
try:
    if withdrawal > balance:
        raise ValueError("Insufficient balance")
    balance = balance - withdrawal
    print("withdrawal successful !")
    print("Remaining balance:",balance)
except ValueError as e:
    print("Insufficient balance:",e)
finally:
    print("Thank you for banking with us!")