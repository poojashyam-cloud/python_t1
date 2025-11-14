# Accept a 3-digit number as input
number = int(input("Enter a 3-digit number: "))
first_digit = number // 100 # Integer division to get the first digit
last_digit = number % 10 # Modulus to get the last digit
sum_of_digits = first_digit + last_digit
print("The sum of the first and last digits is:", sum_of_digits)