#Exercise 1: Alien Colors #1 (Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.)
#•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
#•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

# Passed
# The variable named "alien_color" is assigned to have the value of 'green'.
alien_color = 'green'

# Use "==" to determine if alien_color is equal to 'green'.
if alien_color == 'green':

# Because the condition is met (True), the if statement is executed, which is printing the message "Congratulations! You just earned 5 points!".
    print("Congratulations! You just earned 5 points!")


# Failed
# The variable named "alien_color" is assigned to have the value of 'yellow'.
alien_color = 'yellow'

# Use "==" to determine if alien_color is equal to 'green'.
if alien_color == 'green':

# Because the condition was not met (False), the if statement is not executed.
    print("Congratulations! You just earned 5 points!")
