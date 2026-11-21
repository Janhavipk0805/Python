items = ["apple", "banana", "cherry"]

try:
    index = int(input("Enter an index: "))
    print("Item:", items[index])
except ValueError:
    print("Error: Please enter a valid integer index.")
except IndexError:
    print(f"Error: Index {index} is out of range. "
          f"The list has {len(items)} items (valid indices: 0 to {len(items) - 1}).")