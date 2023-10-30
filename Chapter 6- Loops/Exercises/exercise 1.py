# Exercise 1: Pizza Toppings (Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.)

# The loop that promps the user to enter their chosen topping. It will only end when the user enter the 'quit' value.
prompt = "\nGood day! What topping would you like to be added to your pizza?"
prompt += "\nPlease enter 'quit' when you are finished: "

while True:
    Pizza_Topping = input(prompt)
    if Pizza_Topping != 'quit':
        print(f"  I'll be adding {Pizza_Topping} to your pizza. ")
    else:
        break

print ("Thank you and enjoy your pizza!")