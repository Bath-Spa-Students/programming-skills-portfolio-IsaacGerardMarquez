# Exercise 2: Movie Tickets: (A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket)

# Creating a variable named "Age" that contains a message that would be displayed to the user. 
# The message prompts the user to enter their age.
Age = "Please enter your age :"
# Displays a message to the user saying that they enter "quit" to finish the program.
Age += "\nEnter 'quit' when you are finished: "

# Create a while loop that will continue to run until the user enter the word "quit".
while True:

# Creating an input() function that prompts to get input from the user, which is then stored in the variable named "age".
    age = input(Age)
# If the user enters 'quit', the break statement is executed, which terminates or exits the loop.
    if age == 'quit':
        break
    age = int(age) # Converts the value of age into an integer.

    if age < 3: # If the age is less than 3, it will print the message, "You can watch the movie for free!"
        print("  You can watch the movie for free!")

    elif age < 13: # If the age is between 3 and 13, it will print the message, "The movie ticket will cost you $10."
        print("  The movie ticket will cost you $10.")
    else:
        print("  The movie ticket will cost you $15.") # If the age is egual or greater than 13, it will print the message, "The movie ticket will cost you $15."

# When the program breaks out of the loop, it will then print a message, "Thank you and enjoy your movie!"
print ("Thank you and enjoy your movie!")