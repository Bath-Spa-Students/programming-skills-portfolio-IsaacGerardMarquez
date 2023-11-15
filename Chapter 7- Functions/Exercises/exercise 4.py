# Exercise 4: Large Shirts (Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.)
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Function that would print a large shirt and a medium shirt with the default message, I love Python.
# Define the function named "make_shirt function."
# The parameter named "size" has a default value of 'large' and the parameter named "message" has a default value of "I love Python.".
def make_shirt(size='large', message="I love Python."):

# Creating a print() function to print the string "I made a {size} t-shirt.", where {size} is replaced with the value of the parameter named "size".
    print(f"\nI made a {size} t-shirt.")

# Likewise, printing the string "The message printed on the shirt says, "{message}", where {message} is replaced with the value of the parameter named "message".
    print(f'The message printed on the shirt says, "{message}"')

# Calls the function named "make_shirt" without any arguments.
make_shirt()
# Calls the function named "make_shirt" with the parameter named "size" set to "medium".
make_shirt(size="medium")
# Calls the function named "make_shirt" with both the parameters named "size" and "message" set.
make_shirt("small", "Creative Computing - Group 2.")