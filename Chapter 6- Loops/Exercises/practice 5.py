# Practice 5: Write a Python program that uses a while loop to find the largest number among a series of user-input values until they enter '0' to exit the loop.

# Initialize the variable named "Largest_Number" with a value of 0.
# This is done so that any number that the user input would be larger than the variable.
Largest_Number = float("0")

# Creating a while loop that will run until the user enters "0" to terminate the loop.
while True:
    
# Getting the user input.
    Number = float(input("Please enter a number: "))
    
# When the user enter "0", the break statement terminates the loop. 
    if Number == 0:
        break
    
# Updating the Largest_Number (with the new value) if the current number is larger than it.
    if Number > Largest_Number:
        Largest_Number = Number

# Printing the output which is the largest number.
print("The largest number is", Largest_Number)