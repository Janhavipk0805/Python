# Q7. Generator - Generate Dates for Next 7 Days

from datetime import date, timedelta

# Generator function
def generate_dates():

    today = date.today()

    for i in range(7):
        yield today + timedelta(days=i)


# Calling generator
for d in generate_dates():
    print(d)