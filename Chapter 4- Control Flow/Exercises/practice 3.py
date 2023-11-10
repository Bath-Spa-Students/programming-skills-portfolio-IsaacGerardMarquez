# Write a python program with nested decision structures that perform the following: If amount1 is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2

# Create an input() function that prompts the user to enter a value for the variables named amount1 and amount2.
amount1=int(input("Please enter the value of amount1: "))
amount2=int(input("Please enter the value of amount2: "))

# The first if statement determines if the variable named "amount1" is greater than 10.
if amount1> 10 and amount2< 100:

# The second if statement determines if the variable named "amount2" is less than 100.
    if amount1>amount2:

# If it meets the conditions of the two if statements, it will then print, "The value of amount1 is greater.
        print("The value of amount1 is greater")

# If it does not meet the first condition of the "if statement ", it will then print, "The value of amount2 is greater".
else:
    print("The value of amount2 is greater")
