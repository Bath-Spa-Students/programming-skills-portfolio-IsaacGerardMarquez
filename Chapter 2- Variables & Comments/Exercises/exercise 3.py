#Exercise 3: Stripping Names (Tidy up the code to make it easier to understand Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().)

# A string "\tIsaac Marquez\n" is assigned to the variable named "Name". It has a tab (\t) at the beginning and a newline (\n) at the end.
Name = "\tIsaac Marquez\n"

# The "print ("Unmodified:")" is used to print or output the unmodified or unchanged value of the variable named "Name".
print ("Unmodified:")
print (Name)

# The "print ("\nUsing lstrip():")" is used to print or output the value of the variable named "Name" with leading whitespace removed.
print ("\nUsing lstrip():")
print (Name.lstrip())

# The "print ("\nUsing rstrip():")" is used to print or output the value of the variable named "Name" with trailing whitespace characters removed from the right side (end).
print ("\nUsing rstrip():")
print (Name.rstrip())

# The "print ("\nUsing strip():")" is used to print or output the value of the variable named "Name" with both trailing and leading whitespace characters removed.
print ("\nUsing strip():")
print (Name.strip())