# Exercise 4: Guest List (If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.)

# Creating a list that includes three people that I would like to invite to dinner.
My_Guests = ["Justin Vasquez", "Arthur Nery", "Adie"]

# With the use of the list, print a message to each person, inviting them to dinner.
Name = My_Guests[0].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

Name = My_Guests[1].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

Name = My_Guests[2].title()
print(f"{Name}, I would like to invite you to a dinner at my place.")

print(" ")
print("or") 
print(" ")

names = ["Justin Vasquez", "Arthur Nery", "Adie"]

for name in names:
    print(f'{name}, I would like to invite you to a dinner at my place.')