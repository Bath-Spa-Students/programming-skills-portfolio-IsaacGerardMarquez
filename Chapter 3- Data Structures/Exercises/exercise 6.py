# Exercise 6: Shrinking Guest List (You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.)
# •Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# •Print a message to each of the two people still on your list, letting them know they’re still invited.
# •Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program. 

# Creating a list that includes three people that I would like to invite to dinner.
My_Guests = ["Justin Vasquez", "Arthur Nery", "Adie"]

# With the use of the list, print a message to each person, inviting them to dinner.
Name = My_Guests[0].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

Name = My_Guests[1].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

Name = My_Guests[2].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

# Printing a message that one guest (Arthur Nery) would not be able to come to the dinner.
Name = My_Guests[1].title()
print(f"\nUnfortunately, {Name} would not be able to come to the dinner.")

# Arthur Nery would not be able to come to the dinner. Let us invite Kyle Echarri instead.
# Replace the name of the guest that can't make it with the name of the new person I am inviting.
del(My_Guests[1])
My_Guests.insert(1, 'Kyle Echarri')

# Print a second set of invitation messages, one for each person who is still in your list.
Name = My_Guests[0].title()
print(f"\n{Name}, I would like to invite you to a dinner at my place.")

Name = My_Guests[1].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

Name = My_Guests[2].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

# unfortunately, the table would not be able to arrive on time.
print("\nUnfortunately, we can only invite two people to dinner.")

# Removing one guest using pop.
Name = My_Guests.pop()

print ("My apologies " + Name.title()+ ", due to unforeseen circumstances, we can no longer invite you to the dinner. Sorry, there's no more room available at the table.")

# The two remaining guests that are invited to the dinner.
Name = My_Guests[0].title()
print (Name + ", I would like to invite you to a dinner at my place.")

Name = My_Guests[1].title()
print (Name + ", I would like to invite you to a dinner at my place.")

# Empty out the list.
del(My_Guests[0])
del(My_Guests[0])

# Proving that the list is empty.
print (My_Guests)