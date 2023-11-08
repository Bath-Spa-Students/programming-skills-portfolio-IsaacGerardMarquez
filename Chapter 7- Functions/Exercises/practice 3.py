# Practice 3: Write a Python program that uses a function to check if a given number is prime or not.

# Defining the is_"prime function" to take Number as a parameter.
def is_prime(Number):

# It determines if Number is less than or equal to 1.
    if Number <= 1:

# If it meets the condition, the function returns False because prime numbers are defined as positive integers that are greater than 1.
        return False

# If Number is greater than 1, it creates a loop that iterates from 2 to the square root of Number.
# The loop created determines if Number is divisible by any values that are within the range.
    for i in range(2, int(Number ** 0.5) + 1):

# If Number is divisible by i, the function returns False.
# This indicates the the number is not a prime number.
        if Number % i == 0:
            return False

# The function reaches the return True statement if the loop completes without finding any divisors.
# This indicates that the number is a prime number.
    return True

# Create an input() function that prompts the user to enter a number. The inputted number is then convereted into an integer using int().
Number = int(input("Please enter a number: "))

# Calls the is_prime funtion with the inputted number from "Number" as an argument and determines the returned value.
if is_prime(Number):

# If the returned value is True, it prints or displays that Number is a prime number.
    print(Number, "is a prime number.")

# If the returned value is False, it prints or displays that Number is not a prime number.
else:
    print(Number, "is not a prime number.")