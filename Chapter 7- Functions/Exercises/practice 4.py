# Practice 4: Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius.

# Use "import math" to import the math module in the Python Program.
import math

# Define the calculate_area_circle function that takes the radius of the circle as a parameter.
def calculate_area_circle(Radius):

# The function uses the formula pi * radius^2 to calculate the area of the circle. It is then assigned as the value of "Area".
    Area = math.pi * Radius ** 2

# The function returns the calculated Area.
    return Area

# Create an input() function that prompts the user to enter the Radius of the Circle.
# The inputted number is then convereted into float using float().
Radius = float(input("Please enter the Radius of the Circle: "))

# The calculate_area_circle function is called with the inputted Radius as an argument which then assigns the returned value to the variable named "The_Area_of_a_Circle".
The_Area_of_a_Circle = calculate_area_circle(Radius)

# Create a print() function that would display the Area of the Circle with Radius.
print ("The Area of the Circle with Radius", Radius, "is:", The_Area_of_a_Circle)