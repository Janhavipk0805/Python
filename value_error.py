try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("Error: That was not a valid integer. Please enter a number.")