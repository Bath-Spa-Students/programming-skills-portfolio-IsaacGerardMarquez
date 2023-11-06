#Exercise 3: Print date and Time (Write a Python program to display the current date and time.)

# Use import datetime to import the datetime module.
import datetime

# Creating a variable named "time".
# Used the datetime.now() to retrieve the current date and time.
time = datetime.datetime.now()

# Using the print() function to print or display the output.
print("The current date is ...")
print(time.strftime("%y / %m / %d"))
print("The current time is ...")
print(time.strftime("%I / %M / %S"))
print(" ")

print("Or simply")

print(" ")
# Using the print () function to display the value stored in the variable named "time", which represents the current date and time.
print (time)
print(" ")