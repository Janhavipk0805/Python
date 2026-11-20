# Q5. Map, Filter and Reduce

from functools import reduce

# Given list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# 1. MAP - Generate squares of all numbers
squares = map(lambda i: i*i, numbers)
print(f"Squares are: {list(squares)}")

# 2. FILTER - Extract even numbers
even = filter(lambda i: i%2==0, numbers)
print(f"Even numbers are: {list(even)}")

# 3. REDUCE - Calculate sum of all numbers
s = reduce(lambda x,y: x+y, numbers)
print(f"Sum of numbers is: {s}")