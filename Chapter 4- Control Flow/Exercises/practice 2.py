# Practice 2: Write an if-else statement that assigns O to the variable b if the variable a is less than 10. Otherwise, it should assign 99 to the variable b.

# Create a variable named "a" that stores a value of 39.
a = 39

# Create an if statement that determines if a is less than 10.
# If it meets the condition (True), the code block inside the if statement is executed. Variable "b" is assigned to have the value of "O".
if a < 10:
    b = "O"

# If it does not meet the condition (False), the code block inside the else statement is executed. Variable "b" is assigned to have the value of 99.
else:
    b = 99

# Create a print() function that uses f-string formatting to output the values a and b.
print(f"a = {a}")
print(f"b = {b}")
