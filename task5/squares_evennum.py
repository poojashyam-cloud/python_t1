from functools import reduce

def squares_of_even(nums):
    # Validate input: must be a list of numbers
    if not isinstance(nums, list) or not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("Input must be a list of integers or floats.")

    # Use reduce to accumulate squares of even numbers
    return reduce(
        lambda acc, x: acc + [x ** 2] if x % 2 == 0 else acc,
        nums,
        []
    )

# Example usage
try:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    result = squares_of_even(numbers)
    print("Squares of even numbers:", result)
except ValueError as e:
    print("Error:", e)
