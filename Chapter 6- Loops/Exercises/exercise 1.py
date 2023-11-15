# Exercise 1: Pizza Toppings (Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.)

# Creating a variable named "Topping" that contains a message that would be displayed to the user. 
# The message prompts the user to enter what toppings would be added to their pizza.
Topping = "\nGood day! What topping would you like to be added to your pizza?"
# Creating a second prompt that prompts the user to enter the word "quit" when they are finished with entering the toppings they want on their pizza.
Topping += "\nPlease enter 'quit' when you are finished: "

# Create a while loop that will continue to run until the user enter the word "quit".
while True:
# Creating an input() function that prompts to get input from the user, which is then stored in the variable named "Pizza_Topping".
    Pizza_Topping = input(Topping)

# If the user input is not equal to 'quit', the program will continue to run.
    if Pizza_Topping != 'quit':

# Create a print() function that would display a message to the user about the topping that they have entered. An f-string is also used.
        print(f"  I'll be adding {Pizza_Topping} to your pizza. ")
# If the user inputted or entered the value of 'quit', the program will break out or terminate the loop.
    else:
        break

# Create a print() function that displays a message to the user thanking them for their pizza order and wishing them to enjoy their pizza.
print ("Thank you and enjoy your pizza!")