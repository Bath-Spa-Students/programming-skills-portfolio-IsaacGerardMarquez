# Exercise 3: T-Shirt (Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.)
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# Function that would print a sentence summarizing the size of the shirt and the message printed on it.
def make_shirt(size, message):
    """Summarizing the size of the shirt and the message printed on it."""
    print(f"\nI have an idea of making a personalized {size} t-shirt as a gift for my classmates.")
    print(f'The message printed on the shirt would say, "{message}"')

make_shirt("medium", "Space to Grow!")
make_shirt(message="MAKE YOUR AMBITIONS HAPPEN.", size="small")