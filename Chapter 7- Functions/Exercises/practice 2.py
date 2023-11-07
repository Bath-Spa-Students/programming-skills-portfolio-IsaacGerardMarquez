# Practice 2: Write a Python function that calculates the factorial of a given positive integer using recursion.

# Use a factorial function that takes a positive integer n as input and then calculates its factorial.
def factorial(n):

# If n is equal to 0 or 1, the function returns directly to 1.
    if n == 0 or n == 1:
        return 1
    
# It returns the calculated factorial value for each recursion, multiplying n with the factorial of n-1, and continuing this process.
    return n * factorial(n-1)

# Create a variable named "Positive_Integer" that specifies which positive integer I want to calculate the factorial. In this case, Positive_Integer has a value of 16.
Positive_Integer = 16

# The factorial function returns the calculated factorial value, which is stored in a variable named "Math".
Math = factorial(Positive_Integer)

# Use a f-string formatting to print a message that displays the given positive integer (Positive_Integer) and its factorial (Math).
print (f"The Factorial of {Positive_Integer} (which is the given positive integer) is {Math}.")