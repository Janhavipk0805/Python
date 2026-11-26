units = 500
rate = 0
try:
    bill = units * rate
    effective_units = bill/rate
    print("Calculate:",effective_units)
except ZeroDivisionError as e:
    print("Error:",e)
finally:
    print("Bill calculation completed")