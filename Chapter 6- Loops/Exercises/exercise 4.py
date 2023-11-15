# Exercise 4: Deli (Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.)
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# Creating a List named "sandwich_orders" filled with the names of different sandwiches.
sandwich_orders = ["chicken", "tuna", "cheese", "nutella", "egg", "peanut butter", "ice cream", "jam", "vegetable", "club"]
# Creating an empty list named "finished_sandwiches".
finished_sandwiches = []

# Use while loop to iterate through the list named "sandwich_orders" until it is empty.
while sandwich_orders:

# Use .pop() to remove the first sandwich from the list named "sandwich_orders" and assign it to the variable named "current_sandwich".
    current_sandwich = sandwich_orders.pop()

# Prints a message indicating the the current sandwich is being prepared.
    print(f"I am currently preparing your {current_sandwich} sandwich.")
    
# Use .append() to add the current sandwich to the list named "finished_sandwiches".
    finished_sandwiches.append(current_sandwich)

# In a new line, a message is printed indicating that the sandwich has been finished.
print("\n")
for sandwich in finished_sandwiches:
    print(f"I am finished making your {sandwich} sandwich.")