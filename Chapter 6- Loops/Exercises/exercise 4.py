# Exercise 4: Deli (Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.)
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# List named sandwich_orders filled with the names of different sandwiches.
sandwich_orders = ["chicken", "tuna", "cheese", "nutella", "egg", "peanut butter", "ice cream", "jam", "vegetable", "club"]
# An empty list named finished_sandwiches.
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am currently preparing your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I am finished making your {sandwich} sandwich.")