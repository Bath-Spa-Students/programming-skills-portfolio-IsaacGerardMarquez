#Exercise 5: Compute area of Circle (Write a Python program which accepts the radius of a circle from the user and compute the area.)

import math
radius = float(input("Enter the radius of the circle : "))

area = math.pi * radius * radius

print("The Area of the Circle is : {0}".format(area))