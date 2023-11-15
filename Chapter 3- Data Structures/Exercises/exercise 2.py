# Exercise 2: Greetings (Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.)

# Creating a list called "Names" that would store the names of a few of my friends. The list contains three elements: 'Yyan', 'John', and 'Radjn'.
Names = ['Yyan', 'John', 'Radjn']

# Printing each person with the same message but each personalized with the person’s name.

# Creating a f-string and then assigning it to the variable named "Message". 
# Use the {Names[0].title()}! to access the first element (index 0) from the list named "Names".
Message = f"Long time no see, {Names[0].title()}!"

# Creating a print() function to display the value of the variable named "Message". The personalized message is printed using the first name from the list, which is Yyan.
print (Message)

# Creating a f-string and then assigning it to the variable named "Message". 
# Use the {Names[1].title()}! to access the first element (index 1) from the list named "Names".
Message = f"Long time no see, {Names[1].title()}!"

# Creating a print() function to display the value of the variable named "Message". The personalized message is printed using the second name from the list, which is John.
print (Message)

# Creating a f-string and then assigning it to the variable named "Message". 
# Use the {Names[2].title()}! to access the first element (index 2) from the list named "Names".
Message = f"Long time no see, {Names[2].title()}!"

# Creating a print() function to display the value of the variable named "Message". The personalized message is printed using the third name from the list, which is Radjn.
print (Message)