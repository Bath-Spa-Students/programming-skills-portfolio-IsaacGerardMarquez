# Exercise 2: Movie Tickets: (A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket)

# Loop that asks the users their age, and then tell them the cost of their movie ticket. 
prompt = "Please enter your age :"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You can watch the movie for free!")
    elif age < 13:
        print("  The movie ticket will cost you $10.")
    else:
        print("  The movie ticket will cost you $15.")