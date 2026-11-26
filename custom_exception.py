amount = 25000
withdrawal = 15000
class InsufficientBalanceError(Exception):
    pass
try:
    if withdrawal > amount:
        raise InsufficientBalanceError("Insufficient Balance")
    amount = amount - withdrawal
except InsufficientBalanceError as e:
    print("Insufficient balance:",e)
else:
    print("Withdrawal successful")
    print("Remaining balance:",amount)
finally:
    print("Thank you for banking with us") 