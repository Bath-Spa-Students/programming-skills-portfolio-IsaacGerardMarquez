# Write a python program with an if-else statement that displays Speed is normal if the speed variable is within the range of 24 to 56. If the speed variable's value is outside this range, display 'Speed is abnormal

# Create an input() function that prompts the user to enter the speed.
# The int function is used to convert the value into an integer.
Speed = int(input("Please enter the speed: "))

# Create an if-else statement that determines if the variable named "Speed" is within the range of 24 to 56 with the use of the comparison operators (<= and >=).
# If it meets the condition (True), the code block inside the if statement is executed.
if 24 <= Speed <= 56:
# Create an print() function that would print "The Speed is normal." if it meets the condition.
    print ("Speed is normal.")

# If it does not meet the condition (False), the code block inside the else statement is executed.
else:
# # Create an print() function that would print "Speed is abnormal." if it does not meet the condition.
    print ("The Speed is abnormal.")