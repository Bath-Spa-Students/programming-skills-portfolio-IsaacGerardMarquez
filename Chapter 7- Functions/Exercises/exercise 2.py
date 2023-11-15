# Exercise 2: Favorite Book (Write a function called favorite_book() that accepts one parameter, title.)
# The function should print a message, such as One of my favorite books is Alice in Wonderland. 
# Call the function, making sure to include a book title as an argument in the function call.

# Function that would print a message, such as One of my favorite books is Alice in Wonderland.
# Defining a function and naming it "favorite_book". It also takes a one argument named "title".
def favorite_book(title):

# Creating a print() function to print or display a message. 
# The "{title}" part of the string is replaced with the actual value of the title argument when the function is called.
    print(f"One of my favorite books is {title}.")

# Calls the function named "favorite_book" and passes the argument "Noli Me Tángere".
favorite_book("Noli Me Tángere")
