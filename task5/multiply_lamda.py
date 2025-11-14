# Import the 'reduce' function from the 'functools' module
from functools import reduce
def mutiple_list(nums):
    # Use the 'reduce' function with a lambda to multiply all elements in the 'nums' list
    result = reduce(lambda x, y: x * y, nums)
    # Return the result of multiplying all numbers in the list
    return result

# Create another list 'nums' containing integers
nums = [2, 4, 8, 8, 3, 2, 9]

# Print the original list 'nums' and multiply all its numbers using 'multiple_list' function
print("\nOriginal list:")
print(nums)
print("Multiply all the numbers of the said list:", mutiple_list(nums))
