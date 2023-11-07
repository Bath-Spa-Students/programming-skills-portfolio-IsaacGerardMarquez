# Practice 1: Write a Python function that takes two numbers as arguments and returns their sum.

# In this function, Addition takes two parameters (which is Number1 and Number2) representing the numbers that will added together. 
def Addition (Number1, Number2):

# The function returns the sum Number1 and Number2 using the "+"" operator. 
    The_Sum = Number1 + Number2
    return The_Sum

# Getting the number using user input function.
Number1 = int(input("Please enter the first number: "))
Number2 = int(input("Please enter the second number: "))

# We use Number1 and Number2 as arguments to "Addition" and store the result in the variable named "Sum".
Sum = Addition (Number1, Number2)

# Printing the output which is the sum of the two numbers.
print (Number1, "+", Number2, "=", Sum)