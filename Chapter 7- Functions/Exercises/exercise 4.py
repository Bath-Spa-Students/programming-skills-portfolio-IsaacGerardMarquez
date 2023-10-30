# Exercise 4: Large Shirts (Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.)
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

# Function that would print a large shirt and a medium shirt with the default message, I love Python.
def make_shirt(size='large', message="I love Python."):
    """Summarizing the t shirt that I would be making."""
    print(f"\nI made a {size} t-shirt.")
    print(f'The message printed on the shirt says, "{message}"')

make_shirt()
make_shirt(size="medium")
# Shirt with a different size and message.
make_shirt("small", "Creative Computing - Group 2.")
