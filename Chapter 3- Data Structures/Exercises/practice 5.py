# Practice 5: You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item. Work with the given list:
# list1 = [5, 10, 15, 20, 25, 50, 20]

# Creating a list named list1 that stores [5, 10, 15, 20, 25, 50, 20].
list1 = [5, 10, 15, 20, 25, 50, 20]

# Use index() to find the index of the first occurrence of the value 20 in the list named "list1".
index = list1.index(20)

# Replacing the value of 20 (only the first occurrence) with 200.
list1[index] = 200

# Use print() function to print or display the updated "list1".
print(list1)