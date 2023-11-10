# Given a Python list, write a program to remove all occurrences of item 20.
# Given list:
# list1 = [5, 20, 15, 20, 25, 50, 20]

# Creating a list named list1 that stores the given items.
list1 = [5, 20, 15, 20, 25, 50, 20]

# Create a while loop that would determine if the item 20 is present in the list (list1).
while 20 in list1:

# Use remove() to remove any occurrence of 20 in the list.
    list1.remove(20)

# Use the print() function to print or display the updated list.
print ("The updated list without the item 20 is:", list1)