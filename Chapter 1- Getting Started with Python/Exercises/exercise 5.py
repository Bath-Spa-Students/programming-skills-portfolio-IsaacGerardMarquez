#Exercise 5: Compute area of Circle (Write a Python program which accepts the radius of a circle from the user and compute the area.)

# Use "import math" to import the math module in the Python Program.
import math

# Creating an input() function to let the user enter the radius of the circle.
radius = float(input("Enter the radius of the circle : "))

# Creating a variable named "area" that stores the formula pi multiplied (*) to radius^2.
area = math.pi * radius * radius

# Using the print() funtion to display the output or the calculated area of the circle.
# {0} is used as a place holder for the value of are.
print("The Area of the Circle is : {0}".format(area))