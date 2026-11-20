# Q1. Function Scope and Built-in Functions

def analyze_numbers(*nums):
    print("Maximum Number:", max(nums))
    print("Minimum Number:", min(nums))
    print("Sum of Numbers:", sum(nums))
    print("Average of Numbers:", sum(nums) / len(nums))


# Function call
analyze_numbers(1, 2, 3, 5, 6, 7, 8, 9, 10)