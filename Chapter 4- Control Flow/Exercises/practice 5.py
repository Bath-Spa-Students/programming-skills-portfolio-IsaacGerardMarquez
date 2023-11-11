# Practice 5: Write a Python program that uses the elif statement to determine the season based on the month provided as input.

# Create a determine_season function which would take the month as an input and determines the corresponding season.
def determine_season(month):

# Create an if statement that if meets any of the condition, the corresponding season is then assigned to the variable named "Season".
    if month in ["January", "February", "March"]:
        Season = "Spring"
    
    elif month in ["July", "August", "September"]:
        Season = "Autumn"

    elif month in ["October", "November", "December"]:
        Season = "Winter"

    elif month in ["April", "May", "June"]:
        Season = "Summer"

# If none of the conditions from the if (or elif) statements is met, the else statement assigns the value "Please enter a valid month" to the variable named "Season".
    else:
        Season = "Please enter a valid month:"

# The function returns the determined Season.
    return Season

# Create an input() function that prompts the user to enter a month.
Month = str(input("Please enter the month: "))

# The determine_season function is then called with the month that was inputted by the user as an argument.
# The returned Season value is then stored in the variable named "Season".
Season = determine_season(Month)

# The print() function prints or displays the determined season using f-string formatting.
print (f"The season for the month of {Month} is {Season}.")