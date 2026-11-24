from collections import Counter

items = ["apple", "banana", "apple", "cherry", "banana", "apple",
         "date", "cherry", "banana", "apple"]

item_count = Counter(items)

print("Top 3 most common elements:")
for item, count in item_count.most_common(3):
    print(f"  {item}: {count}")