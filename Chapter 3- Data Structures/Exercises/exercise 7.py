# Exercise 7: Seeing the World (Think of at least five places in the world you’d like to visit. • Store the locations in a list. Make sure the list is not in alphabetical order.)
# • Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

# Creating a list that would store the five places in the world that I would like to visit.
My_Dream_Destinations = ['Palawan', 'Disney Land', 'Eiffel Tower', 'Ferrari World', 'Sea World']

# Printing the list in its original order.
print("Original order:")
print(My_Dream_Destinations)

# Printing the list using sorted() to print the list in alphabetical order.
print("\nAlphabetical:")
print(sorted(My_Dream_Destinations))

# Printing the list showing that the list is still in its original order. 
print("\nOriginal order:")
print(My_Dream_Destinations)

# Printing the list using sorted() to print the list in reverse alphabetical order without changing the order of the original list.
print("\nReverse alphabetical:")
print(sorted(My_Dream_Destinations, reverse=True))

# Printing the list again to show that the list is still in its original order.
print("\nOriginal order:")
print(My_Dream_Destinations)

# Printing the list using reverse() to change the order of the list and show that its order has changed.
print("\nReversed:")
My_Dream_Destinations.reverse()
print(My_Dream_Destinations)

# Printing the list using reverse() to change the order of the list again and show that it’s back to its original order.
print("\nOriginal order:")
My_Dream_Destinations.reverse()
print(My_Dream_Destinations)

# Printing the list using sort() to change the list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("\nAlphabetical")
My_Dream_Destinations.sort()
print(My_Dream_Destinations)

# Printing the list using sort() to change the list so it’s stored in reverse alphabetical order.
print("\nReverse alphabetical")
My_Dream_Destinations.sort(reverse=True)
print(My_Dream_Destinations)