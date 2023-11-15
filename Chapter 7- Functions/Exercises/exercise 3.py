# Exercise 3: T-Shirt (Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.)
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# Function that would print a sentence summarizing the size of the shirt and the message printed on it.
# Defining the function named "make_shirt" and specifying that it takes two parameters, which are "size" and "message".
def make_shirt(size, message):

# Printing a statement about the size of the t-shirt. An f-string enabled the program to include the parameter "size" inside the string.
    print(f"\nI have an idea of making a personalized {size} t-shirt as a gift for my classmates.")
# Printing a statement about the message shown on the t-shirt. An f-string enabled the program to include the parameter "message" inside the string.
    print(f'The message printed on the shirt would say, "{message}"')

# Calls the function named make_shirt with the arguments "medium" for size and "Space to Grow!" for message.
make_shirt("medium", "Space to Grow!")
# Calls the function named make_shirt with the arguments "small" for size and "MAKE YOUR AMBITIONS HAPPEN." for message.
make_shirt(message="MAKE YOUR AMBITIONS HAPPEN.", size="small")