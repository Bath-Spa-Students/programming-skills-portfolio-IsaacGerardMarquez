# Practice 4: Commpute the area of triangle.

# Create an input() function that prompts the user to enter the lengths of the sides of a triangle.
# The float() is used to convert the input to a float (decimal number).
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# Calculate the semi-perimeter of the triangle usng the formula "s= (a + b + c) / 2".
# "a", "b", and "c" are the lengths of the sides that were inputted by the user.
s= (a + b + c) / 2

# The Heron's formula is used to calculate the area of the triangle.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

# Create a print() function to display or output the calculated area of the triangle.
# The "%0.2f" is used to display the value of "area" with two decimal places or points.
print('The area of the triangle is %0.2f' %area)
