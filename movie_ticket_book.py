available_seats = 10
requested_seats = 8
try:
    if requested_seats > available_seats:
        raise ValueError("Seats are unavailable")
except ValueError as e:
    print("Seats are unavailable:",e)
else:
    available_seats = available_seats - requested_seats
    print("Remaining seats:",available_seats)
    print("Successful booking")
finally:
    print("thank you for booking !")