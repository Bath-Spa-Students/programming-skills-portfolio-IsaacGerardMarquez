# Exercise 5: Change Guest List (You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.)
# •Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# •Print a second set of invitation messages, one for each person who is still in your list.

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