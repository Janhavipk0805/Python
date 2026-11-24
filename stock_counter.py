from collections import Counter

stock = ["apple", "apple", "apple", "banana", "banana", "cherry"]
sold  = ["apple", "apple", "banana", "cherry", "cherry"]

stock_counter = Counter(stock)
sold_counter  = Counter(sold)

print("Stock :", dict(stock_counter))
print("Sold  :", dict(sold_counter))

# The - operator keeps only positive results
remaining = stock_counter - sold_counter

print("\nRemaining stock (positive counts only):")
for item, count in remaining.items():
    print(f"  {item}: {count}")

# subtract() keeps zero and negative values
stock_counter.subtract(sold_counter)
print("\nAfter .subtract() (includes zero and negative):")
for item, count in stock_counter.items():
    print(f"  {item}: {count}")