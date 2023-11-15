#Exercise 2: Alien Colors #2 (Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.)
#•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
#•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
#•Write one version of this program that runs the if block and another that runs the else block.

# Program that runs the if block
# The variable named "alien_color" is assigned to have the value of "green".
alien_color = "green"

# Use "==" to determine if alien_color is equal to 'green'. The if block would only be executed if alien_color is equal to green.
if alien_color == "green":
# Since the condition is met (True), the if statement if executed, which prints the message "Congratulations on shooting the alien! You just earned 5 points!".
    print("Congratulations on shooting the alien! You just earned 5 points!")

# If the condition was not met (False), the else statement will be executed, which prints the message "Congratulations! You just earned 10 points!".
else:
    print("Congratulations! You just earned 10 points!")


# Program that runs the else block
# The variable named "alien_color" is assigned to have the value of "orange".
alien_color = "orange"

# Use "==" to determine if alien_color is equal to 'green'.
if alien_color == "green":
# If the condition is met (True), the if statement will be executed, which prints the message "Congratulations on shooting the alien! You just earned 5 points!".
    print("Congratulations on shooting the alien! You just earned 5 points!")

# However, because the condition was not met (False), the else statement is executed, which prints the message "Congratulations! You just earned 10 points!".
else:
    print("Congratulations! You just earned 10 points!")