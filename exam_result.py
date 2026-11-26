marks = 20
try:
    if marks <0 or marks > 100:
        raise ValueError("Please enter valid marks")
except ValueError as e:
    print("Please enter valid marks:",e)
else:
     print("Valid marks")
finally:
    print("Result processing completed")